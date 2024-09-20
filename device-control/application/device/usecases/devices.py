import uuid
from application.device.models.device import RegisterDeviceInput, RegisterDeviceRaw, EditDeviceInput
from application.device.models.device import CommandInput
from application.device.usecases.interfaces import DeviceRegisterRepoInterface, DeviceGetRepoInterface, \
    DeviceGetAllRepoInterface, DeviceUpdateRepoInterface, DeviceDeleteRepoInterface, DeviceCommandExecuteRepoInterface


class RegisterDeviceUseCase:
    def __init__(self, device_repo: DeviceRegisterRepoInterface):
        self._device_repo = device_repo

    async def execute(self, device: RegisterDeviceInput):
        new_id = uuid.uuid4()
        await self._device_repo.save_new_device(RegisterDeviceRaw(id=new_id, **device.model_dump()))


class GetDevicesUseCase:
    def __init__(self, device_repo: DeviceGetAllRepoInterface):
        self._device_repo = device_repo

    def execute(self, user_id: uuid.UUID):
       return self._device_repo.get_all_devices(user_id=user_id)


class GetSingleDeviceUseCase:
    def __init__(self, device_repo: DeviceGetRepoInterface):
        self._device_repo = device_repo

    def execute(self, device_id: uuid.UUID, user_id: uuid.UUID):
        return self._device_repo.get_device(device_id=device_id, user_id=user_id)


class UpdateDeviceUseCase:
    def __init__(self, device_repo: DeviceUpdateRepoInterface):
        self._device_repo = device_repo

    def execute(self, device_id: uuid.UUID, user_id: uuid.UUID, device: EditDeviceInput):
        self._device_repo.update_device(device_id=device_id, user_id=user_id, device=device)


class DeleteDeviceUseCase:
    def __init__(self, device_repo: DeviceDeleteRepoInterface):
        self._device_repo = device_repo

    def execute(self, device_id: uuid.UUID, user_id: uuid.UUID):
        self._device_repo.delete_device(device_id=device_id, user_id=user_id)


class ExecuteCommandUseCase:
    def __init__(self, command_executor: DeviceCommandExecuteRepoInterface):
        self._command_executor = command_executor

    def execute(self, device_id: uuid.UUID, user_id: uuid.UUID, commands: list[CommandInput]):
        self._command_executor.execute_command(device_id=device_id, user_id=user_id, commands=commands)
