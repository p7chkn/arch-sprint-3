import asyncio
import json
import signal

from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError

from application.device.models.device import DeviceInfoCreate
from application.device.usecases.device_info import CreateDeviceInfoUseCase
from config import config
from infrastructure.postgres.device import DeviceInfoRepo
from infrastructure.postgres.session import create_session


async def consume():
    consumer = AIOKafkaConsumer(
        config.device_topic,
        bootstrap_servers=config.kafka_broker,
    )

    retries = 10
    for i in range(retries):
        try:
            await consumer.start()
            print(f"Start consuming from {config.device_topic}, from {config.kafka_broker}")
            break
        except KafkaConnectionError:
            print(f"Kafka is not ready, retrying in 5 seconds... ({i + 1}/{retries})")
            await asyncio.sleep(5)

    async def process_message(msg):
        print(f"Consumed message: {msg.value.decode('utf-8')}")
        try:
            value = msg.value.decode("utf-8")
            data = json.loads(value)
        except Exception as e:
            print(f"Error while consuming message {e}")
            return
        session = create_session()
        repo = DeviceInfoRepo(session)
        use_case = CreateDeviceInfoUseCase(repo)
        try:
            await use_case.execute(device_info=DeviceInfoCreate(
                device_link=data["device_link"],
                user_id=data["user_id"],
                device_id=data["id"],
            ))
            session.commit()
        except Exception as e:
            print(f"Error while consuming message {e}")
        finally:
            session.close()

    async def consume_messages():
        try:
            async for msg in consumer:
                await process_message(msg)
        finally:
            await consumer.stop()

    # Create a Task for consuming messages
    consume_task = asyncio.create_task(consume_messages())

    # Wait for the signal to stop the consumer
    try:
        await consume_task
    except asyncio.CancelledError:
        print("Consumer task was cancelled.")


async def shutdown(loop, signal=None):
    """Cleanup tasks tied to the service's shutdown."""
    if signal:
        print(f"Received exit signal {signal.name}...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    for task in tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

    loop.stop()


def run():
    loop = asyncio.get_event_loop()

    signals = (signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(loop, signal=s)))

    try:
        loop.run_until_complete(consume())
    finally:
        loop.run_until_complete(asyncio.sleep(0.1))
        loop.close()


if __name__ == "__main__":
    run()
