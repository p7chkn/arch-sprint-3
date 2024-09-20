from fastapi.params import Depends

from application.device.usecases.devices import RegisterDeviceUseCase, GetDevicesUseCase, GetSingleDeviceUseCase, \
    DeleteDeviceUseCase, UpdateDeviceUseCase, ExecuteCommandUseCase
from application.device.usecases.interfaces import DeviceRegisterRepoInterface, DeviceGetRepoInterface, \
    DeviceGetAllRepoInterface, DeviceUpdateRepoInterface, DeviceDeleteRepoInterface, DeviceCommandExecuteRepoInterface
from infrastructure.mock.services import MockDeviceCommandExecutor
from presentation.api.dependencies.db import get_device_register_repo


def get_device_register_use_case(device_repo: DeviceRegisterRepoInterface = Depends(get_device_register_repo)) -> RegisterDeviceUseCase:
    return RegisterDeviceUseCase(device_repo=device_repo)

def get_devices_get_use_case(device_repo: DeviceGetAllRepoInterface = Depends(get_device_register_repo)) -> GetDevicesUseCase:
   return GetDevicesUseCase(device_repo=device_repo)

def get_single_get_use_case(device_repo: DeviceGetRepoInterface = Depends(get_device_register_repo)) -> GetSingleDeviceUseCase:
    return GetSingleDeviceUseCase(device_repo=device_repo)

def get_edit_device_use_case(device_repo: DeviceUpdateRepoInterface = Depends(get_device_register_repo)) -> UpdateDeviceUseCase:
    return UpdateDeviceUseCase(device_repo=device_repo)

def get_delete_device_use_case(device_repo: DeviceDeleteRepoInterface = Depends(get_device_register_repo)) -> DeleteDeviceUseCase:
    return DeleteDeviceUseCase(device_repo=device_repo)

def get_command_executor() -> DeviceCommandExecuteRepoInterface:
    return MockDeviceCommandExecutor()

def get_command_execute_use_case(command_executor: DeviceCommandExecuteRepoInterface = Depends(get_command_executor)) -> ExecuteCommandUseCase:
    return ExecuteCommandUseCase(command_executor=command_executor)
