from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Log(BaseModel):
    id: UUID
    log_datetime: datetime
    device_id: UUID
    value: str


class NewLogInfo(BaseModel):
    device_id: UUID
    value: str
    log_datetime: datetime