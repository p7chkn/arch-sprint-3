from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class LogResponse(BaseModel):
    id: UUID
    log_datetime: datetime
    device_id: UUID
    value: str
