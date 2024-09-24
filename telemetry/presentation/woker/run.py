import asyncio
import signal
from application.device.usecases.device_call import DeviceCallUseCase
from application.device.usecases.device_info import GetDeviceInfoUseCase
from application.log.models.log import NewLogInfo
from application.log.usecases.log import CreateNewLogUseCase
from infrastructure.mock.caller import MockCaller
from infrastructure.postgres.device import DeviceInfoRepo
from infrastructure.postgres.log import LogRepo
from infrastructure.postgres.session import create_session
from config import config

stop_event = None


async def main():
    global stop_event
    stop_event = asyncio.Event()

    loop = asyncio.get_running_loop()

    def shutdown_signal_handler():
        print("Shutdown signal received")
        stop_event.set()

    loop.add_signal_handler(signal.SIGTERM, shutdown_signal_handler)
    loop.add_signal_handler(signal.SIGINT, shutdown_signal_handler)

    while not stop_event.is_set():
        session = create_session()
        get_all_device_info = GetDeviceInfoUseCase(DeviceInfoRepo(session))
        save_log_info = CreateNewLogUseCase(LogRepo(session))
        call_device_use_case = DeviceCallUseCase(MockCaller())
        device_info = await get_all_device_info.execute()
        for device in device_info:
            response = await call_device_use_case.execute(device_link=device.device_link)
            if response:
                await save_log_info.execute(NewLogInfo(
                    device_id=device.id,
                    value=response.value,
                    log_datetime=response.date,
                ))
        session.commit()
        session.close()

        try:
            await asyncio.wait_for(stop_event.wait(), timeout=config.polling_delay_seconds)
        except asyncio.TimeoutError:
            continue

    print("Shutting down gracefully")


def run():
    asyncio.run(main())


if __name__ == '__main__':
    run()
