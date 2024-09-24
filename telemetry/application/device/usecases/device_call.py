from application.device.models.device_response import DeviceResponse
from application.device.usecases.interfaces import DeviceCallerInterface


class DeviceCallUseCase:
    def __init__(self, caller: DeviceCallerInterface):
        self._caller = caller

    async def execute(self, device_link: str) -> DeviceResponse:
        info = await self._caller.call_device(device_link)
        return info