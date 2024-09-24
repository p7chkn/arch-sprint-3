from uuid import UUID

from sqlalchemy.orm import Mapped

from infrastructure.postgres.models.base import BaseModel


class DeviceInfo(BaseModel):
    __tablename__ = "device_info"

    user_id: Mapped[UUID]
    device_id: Mapped[UUID]
    device_link: Mapped[str]
