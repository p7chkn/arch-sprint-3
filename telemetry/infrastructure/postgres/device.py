from sqlalchemy.orm import Session

from application.device.models.device import DeviceInfoModel
from application.device.usecases.interfaces import SaveDeviceInfoInterface, GetAllDevicesInfoInterface
from infrastructure.postgres.models.device import DeviceInfo


class DeviceInfoRepo(SaveDeviceInfoInterface, GetAllDevicesInfoInterface):
    def __init__(self, session: Session):
        self._session = session

    async def save_device_info(self, device_info: DeviceInfoModel):
        self._session.add(DeviceInfo(
            id=device_info.id,
            device_id=device_info.device_id,
            user_id=device_info.user_id,
            device_link=device_info.device_link,
        ))

    async def get_all_devices_info(self) -> list[DeviceInfoModel]:
        devices = self._session.query(DeviceInfo).all()
        return [convert_db_to_model(device) for device in devices]


def convert_db_to_model(device: DeviceInfo) -> DeviceInfoModel:
    return DeviceInfoModel(
        id=device.id,
        device_id=device.device_id,
        user_id=device.user_id,
        device_link=device.device_link,
    )
