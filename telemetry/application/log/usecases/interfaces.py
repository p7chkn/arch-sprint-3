from typing import Protocol
from uuid import UUID

from application.log.models.log import Log


class DeviceStatusRepoInterface(Protocol):
    async def get_device_status(self, device_id: UUID) -> Log:
        ...

class LogsByDeviceRepoInterface(Protocol):
    async def get_logs_by_device(self, device_id: UUID) -> list[Log]:
        ...

class SaveLogInterface(Protocol):
    async def save_log(self, log: Log):
        ...
