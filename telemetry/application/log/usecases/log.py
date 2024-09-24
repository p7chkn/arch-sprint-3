import uuid
from datetime import datetime

from application.log.models.log import Log, NewLogInfo
from application.log.usecases.interfaces import LogsByDeviceRepoInterface, DeviceStatusRepoInterface, SaveLogInterface

class GetDeviceStatusUseCase:
    def __init__(self, log_repo: DeviceStatusRepoInterface):
        self._log_repo = log_repo

    async def execute(self, device_id: uuid.UUID) -> Log:
        log = await self._log_repo.get_device_status(device_id=device_id)
        return log

class GetLogsUseCase:
    def __init__(self, log_repo: LogsByDeviceRepoInterface):
        self._log_repo = log_repo

    async def execute(self, device_id: uuid.UUID) -> list[Log]:
        logs = await self._log_repo.get_logs_by_device(device_id)
        return logs

class CreateNewLogUseCase:
    def __init__(self, log_repo: SaveLogInterface):
        self._log_repo = log_repo

    async def execute(self, log: NewLogInfo):
        new_id = uuid.uuid4()

        await self._log_repo.save_log(log=Log(
            id=new_id,
            log_datime=log.log_datetime,
            **log.model_dump(),
        ))
