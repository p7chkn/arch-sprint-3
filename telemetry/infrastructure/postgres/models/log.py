import uuid
from datetime import datetime

from sqlalchemy.orm import Mapped

from infrastructure.postgres.models.base import BaseModel


class TelemetryLog(BaseModel):
    __tablename__ = "telemetry_log"

    log_datetime: Mapped[datetime]
    device_id: Mapped[uuid.UUID]
    value: Mapped[str]
