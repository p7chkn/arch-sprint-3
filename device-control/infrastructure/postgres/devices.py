from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from application.device.models.device import RegisterDeviceRaw, EditDeviceInput
from application.device.usecases.interfaces import DeviceRegisterRepoInterface, DeviceGetRepoInterface, \
    DeviceGetAllRepoInterface, DeviceDeleteRepoInterface, DeviceUpdateRepoInterface
from infrastructure.postgres.models.device import Device


class DeviceRepo(DeviceRegisterRepoInterface,
                 DeviceGetRepoInterface,
                 DeviceGetAllRepoInterface,
                 DeviceDeleteRepoInterface,
                 DeviceUpdateRepoInterface):
    def __init__(self, session: Session):
        self._session = session

    async def save_new_device(self, device: RegisterDeviceRaw):
        self._session.add(Device(
            id=device.id,
            title=device.title,
            module_id=device.module_id,
            user_id=device.user_id,
            device_type=device.device_type,
            device_vendor=device.device_vendor,
            device_link=device.device_link,
            serial_number=device.serial_number,
        ))

    async def get_device(self, device_id: UUID, user_id: UUID) -> RegisterDeviceRaw:
        device: Optional[Device] = (self._session.query(Device).
                                    filter(Device.id == device_id,
                                           Device.user_id == user_id).
                                    one_or_none())
        if not device:
            return None
        return convert_db_to_dto(device=device)

    async def get_all_devices(self, user_id: UUID) -> list[RegisterDeviceRaw]:
        devices = self._session.query(Device).filter(Device.user_id == user_id).all()

        return [convert_db_to_dto(device) for device in devices]

    async def update_device(self, device_id: UUID, user_id: UUID, device: EditDeviceInput):
        device_to_update = (self._session.query(Device)
                            .filter(Device.id == device_id, Device.user_id == user_id)
                            .one_or_none())

        if not device_to_update:
            return None

        device_to_update.title = device.title
        device_to_update.module_id = device.module_id


    async def delete_device(self, device_id: UUID, user_id: UUID):
        device_to_delete = (self._session.query(Device)
                            .filter(Device.id == device_id, Device.user_id == user_id)
                            .one_or_none())

        if not device_to_delete:
            return None

        self._session.delete(device_to_delete)
        self._session.commit()
        return True


def convert_db_to_dto(device: Device) -> RegisterDeviceRaw:
    return RegisterDeviceRaw(
        id=device.id,
        module_id=device.module_id,
        title=device.title,
        device_type=device.device_type,
        device_vendor=device.device_vendor,
        serial_number=device.serial_number,
        device_link=device.device_link,
        user_id=device.user_id,
    )