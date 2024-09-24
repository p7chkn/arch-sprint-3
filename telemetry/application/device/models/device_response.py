from datetime import datetime

from pydantic import BaseModel


class DeviceResponse(BaseModel):
    date: datetime
    value: str
