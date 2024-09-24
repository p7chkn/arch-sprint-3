from fastapi.params import Depends

from application.log.usecases.log import GetLogsUseCase, GetDeviceStatusUseCase, CreateNewLogUseCase
from application.log.usecases.interfaces import LogsByDeviceRepoInterface, DeviceStatusRepoInterface, SaveLogInterface
from presentation.dependencies.db import get_log_repo


def get_logs_use_case(log_repo: LogsByDeviceRepoInterface = Depends(get_log_repo)) -> GetLogsUseCase:
    return GetLogsUseCase(log_repo=log_repo)

def get_device_status_use_case(log_repo: DeviceStatusRepoInterface = Depends(get_log_repo)) -> GetDeviceStatusUseCase:
    return GetDeviceStatusUseCase(log_repo=log_repo)

def save_device_status_use_case(log_repo: SaveLogInterface = Depends(get_log_repo)) -> CreateNewLogUseCase:
    return CreateNewLogUseCase(log_repo=log_repo)
