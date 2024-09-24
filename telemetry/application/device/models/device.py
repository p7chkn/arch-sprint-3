from uuid import UUID

from pydantic import BaseModel


class DeviceInfoCreate(BaseModel):
    device_id: UUID
    user_id: UUID
    device_link: str

class DeviceInfoModel(DeviceInfoCreate):
    id: UUID
    device_id: UUID
    user_id: UUID
    device_link: str
