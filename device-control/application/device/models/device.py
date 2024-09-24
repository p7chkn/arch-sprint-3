from enum import Enum
from uuid import UUID

import pydantic


class DeviceType(str, Enum):
    temperature_sensor = "temperature_sensor"
    move_sensor = "move_sensor"

class DeviceVendor(str, Enum):
    yandex = "yandex"
    xiaomi = "xiaomi"

class RegisterDeviceInput(pydantic.BaseModel):
    module_id: UUID
    title: str
    device_type: DeviceType
    device_vendor: DeviceVendor
    serial_number: str
    device_link: str
    user_id: UUID

class RegisterDeviceRaw(RegisterDeviceInput):
    id: UUID


class EditDeviceInput(pydantic.BaseModel):
    title: str
    module_id: UUID

class CommandInput(pydantic.BaseModel):
    command: str
    arguments: list[str]
