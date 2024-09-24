from fastapi.params import Depends

from application.device.usecases.device_call import DeviceCallUseCase
from application.device.usecases.device_info import GetDeviceInfoUseCase, CreateDeviceInfoUseCase
from application.device.usecases.interfaces import SaveDeviceInfoInterface, GetAllDevicesInfoInterface, \
    DeviceCallerInterface
from presentation.dependencies.caller import get_device_caller
from presentation.dependencies.db import get_device_info_repo


def get_device_info_use_case(repo: GetAllDevicesInfoInterface = Depends(get_device_info_repo)) -> GetDeviceInfoUseCase:
    return GetDeviceInfoUseCase(repo)

def create_device_info_use_case(repo: SaveDeviceInfoInterface = Depends(get_device_info_repo)) -> CreateDeviceInfoUseCase:
    return CreateDeviceInfoUseCase(repo)

def device_call_use_case(caller:DeviceCallerInterface = Depends(get_device_caller)) -> DeviceCallUseCase:
    return DeviceCallUseCase(caller=caller)
