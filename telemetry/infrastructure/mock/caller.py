from datetime import datetime

from application.device.models.device_response import DeviceResponse
from application.device.usecases.interfaces import DeviceCallerInterface


class MockCaller(DeviceCallerInterface):
    async def call_device(self, device_link: str) -> DeviceResponse:
        return DeviceResponse(
            date=datetime.now(),
            value="test",
        )