from typing import Optional
from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session

from infrastructure.postgres.models.log import TelemetryLog
from application.log.models.log import Log
from application.log.usecases.interfaces import DeviceStatusRepoInterface, SaveLogInterface, LogsByDeviceRepoInterface

class LogRepo(DeviceStatusRepoInterface,
              SaveLogInterface,
              LogsByDeviceRepoInterface):
    def __init__(self, session: Session):
        self._session = session

    async def get_device_status(self, device_id: UUID) -> Log:
        log = (self._session.query(TelemetryLog)
           .filter(TelemetryLog.device_id == device_id)
           .order_by(desc(TelemetryLog.created_at))
           .first())
        if not log:
            return None

        return convert_db_to_dto(log)

    async def get_logs_by_device(self, device_id: UUID) -> list[Log]:
        logs = (self._session.query(TelemetryLog)
                .filter(TelemetryLog.device_id == device_id)
                .order_by(desc(TelemetryLog.created_at))
                ).all()

        return [convert_db_to_dto(log) for log in logs]

    async def save_log(self, log: Log):
        self._session.add(TelemetryLog(
            id=log.id,
            log_datetime=log.log_datetime,
            device_id=log.device_id,
            value=log.value,
        ))

def convert_db_to_dto(log: TelemetryLog) -> Log:
    return Log(
        id=log.id,
        log_datetime=log.log_datetime,
        device_id=log.device_id,
        value=log.value,
    )
