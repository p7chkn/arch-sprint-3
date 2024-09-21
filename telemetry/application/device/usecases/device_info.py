import uuid

from application.device.models.device import DeviceInfoCreate, DeviceInfoModel
from application.device.usecases.interfaces import SaveDeviceInfoInterface, GetAllDevicesInfoInterface


class CreateDeviceInfoUseCase:
    def __init__(self, device_info_repo: SaveDeviceInfoInterface):
        self._repo = device_info_repo

    async def execute(self, device_info: DeviceInfoCreate):
        new_id = uuid.uuid4()
        await self._repo.save_device_info(device_info=DeviceInfoModel(
            id=new_id,
            **device_info.model_dump(),
        ))

class GetDeviceInfoUseCase:
    def __init__(self, device_info_repo: GetAllDevicesInfoInterface):
        self._repo = device_info_repo

    async def execute(self) -> list[DeviceInfoModel]:
        devices = await self._repo.get_all_devices_info()
        return devices
