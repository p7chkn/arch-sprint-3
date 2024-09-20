from typing import Protocol
from uuid import UUID

from application.device.models.device import RegisterDeviceRaw, EditDeviceInput
from application.device.models.device import CommandInput


class DeviceRegisterRepoInterface(Protocol):
    async def save_new_device(self, device: RegisterDeviceRaw):
        ...

class DeviceGetRepoInterface(Protocol):
    async def get_device(self, device_id: UUID, user_id: UUID) -> RegisterDeviceRaw:
        ...

class DeviceGetAllRepoInterface(Protocol):
    async def get_all_devices(self, user_id: UUID) -> list[RegisterDeviceRaw]:
        ...

class DeviceUpdateRepoInterface(Protocol):
    async def update_device(self, device_id: UUID, user_id: UUID, device: EditDeviceInput):
        ...

class DeviceDeleteRepoInterface(Protocol):
    async def delete_device(self, device_id: UUID, user_id: UUID):
        ...

class DeviceCommandExecuteRepoInterface(Protocol):
    async def execute_command(self, device_id: UUID, user_id: UUID, commands: list[CommandInput]):
        ...
