import uuid

from application.device.models.device import RegisterDeviceRaw, DeviceType, DeviceVendor, EditDeviceInput
from application.device.usecases.interfaces import DeviceRegisterRepoInterface, DeviceGetRepoInterface, \
    DeviceGetAllRepoInterface, DeviceDeleteRepoInterface, DeviceUpdateRepoInterface


class MockDeviceRepo(DeviceRegisterRepoInterface,
                     DeviceGetRepoInterface,
                     DeviceGetAllRepoInterface,
                     DeviceDeleteRepoInterface,
                     DeviceUpdateRepoInterface):
    async def save_new_device(self, device: RegisterDeviceRaw):
        print(f"pretending to save device {device}")

    async def get_device(self,
                         device_id: uuid.UUID,
                         user_id: uuid.UUID) -> RegisterDeviceRaw:
        print(f"pretending to get device {device_id} for user {user_id}")
        return RegisterDeviceRaw(
            id=uuid.uuid4(),
            title="My device",
            device_type=DeviceType.move_sensor,
            device_vendor=DeviceVendor.yandex,
            serial_number="serial_number",
            device_link="some_link",
            user_id=user_id,
        )

    async def get_all_devices(self, user_id: uuid.UUID) -> list[RegisterDeviceRaw]:
        print(f"pretending to get all devices for user {user_id}")
        return [
            RegisterDeviceRaw(
                id=uuid.uuid4(),
                title="My device",
                device_type=DeviceType.move_sensor,
                device_vendor=DeviceVendor.yandex,
                serial_number="serial_number",
                device_link="some_link",
                user_id=user_id,
            ),
            RegisterDeviceRaw(
                id=uuid.uuid4(),
                title="My device 2",
                device_type=DeviceType.temperature_sensor,
                device_vendor=DeviceVendor.xiaomi,
                serial_number="serial_number",
                device_link="some_link",
                user_id=user_id,
            ),
        ]

    async def update_device(self,
                            device_id: uuid.UUID,
                            user_id: uuid.UUID,
                            device: EditDeviceInput):
        print(f"pretending to update device {device_id} for user {user_id}")

    async def delete_device(self, device_id: uuid.UUID, user_id: uuid.UUID):
        print(f"pretending to delete device {device_id} for user {user_id}")
