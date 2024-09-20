from uuid import UUID

from pydantic import BaseModel

from application.device.models.device import DeviceType, DeviceVendor


class RegisterDeviceRequest(BaseModel):
    module_id: UUID
    title: str
    device_type: DeviceType
    device_vendor: DeviceVendor
    serial_number: str
    device_link: str

class EditDeviceRequest(BaseModel):
    title: str
    module_id: UUID

class ResponseDevice(BaseModel):
    id: UUID
    title: str
    device_type: DeviceType
    device_vendor: DeviceVendor
    serial_number: str
    device_link: str
    user_id: UUID
