import uuid

from sqlalchemy.orm import Mapped

from infrastructure.postgres.models.base import BaseModel


class Device(BaseModel):
    __tablename__ = "devices"

    title: Mapped[str]
    module_id: Mapped[uuid.UUID]
    user_id: Mapped[uuid.UUID]
    device_type: Mapped[str]
    device_vendor: Mapped[str]
    serial_number: Mapped[str]
    device_link: Mapped[str]
