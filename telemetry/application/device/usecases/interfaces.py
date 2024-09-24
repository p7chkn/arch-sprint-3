from typing import Protocol

from application.device.models.device import DeviceInfoModel
from application.device.models.device_response import DeviceResponse


class SaveDeviceInfoInterface(Protocol):
    async def save_device_info(self, device_info: DeviceInfoModel):
        ...

class GetAllDevicesInfoInterface(Protocol):
    async def get_all_devices_info(self) -> list[DeviceInfoModel]:
        ...

class DeviceCallerInterface(Protocol):
    async def call_device(self, device_link: str) -> DeviceResponse:
        ...