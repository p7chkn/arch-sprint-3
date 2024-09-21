from aiokafka import AIOKafkaProducer
from application.device.models.device import RegisterDeviceRaw
from application.device.usecases.interfaces import DevicePublishInterface

from config import config


class KafkaPublisher(DevicePublishInterface):
    def __init__(self):
        self.kafka_broker = config.kafka_broker
        self.producer = None
        self.topic = config.device_topic

    async def start(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.kafka_broker,
        )
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()

    async def publish_device(self, device: RegisterDeviceRaw):
        if self.producer is None:
            await self.start()

        device_data = device.model_dump_json().encode("utf-8")

        await self.producer.send_and_wait(self.topic, device_data)
