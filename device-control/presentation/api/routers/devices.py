import http

from fastapi import APIRouter, Depends, Response
from uuid import UUID

from application.device.models.device import RegisterDeviceInput, EditDeviceInput
from application.device.usecases.devices import RegisterDeviceUseCase, GetDevicesUseCase, GetSingleDeviceUseCase, \
    UpdateDeviceUseCase, DeleteDeviceUseCase, ExecuteCommandUseCase
from presentation.api.dependencies.device import get_device_register_use_case, get_single_get_use_case, \
    get_devices_get_use_case, get_edit_device_use_case
from presentation.api.dependencies.request import get_user_id
from presentation.api.routers.schemas.devices import RegisterDeviceRequest, ResponseDevice

router = APIRouter(
    prefix="",
    tags=["devices"],
)


@router.post("/register")
async def register_device(
        new_device: RegisterDeviceRequest,
        user_id: UUID = Depends(get_user_id),
        register_use_case: RegisterDeviceUseCase = Depends(get_device_register_use_case),
):
    await register_use_case.execute(device=RegisterDeviceInput(user_id=user_id, **new_device.dict()))
    return Response(status_code=http.HTTPStatus.CREATED)


@router.get("/",  response_model=list[ResponseDevice], status_code=http.HTTPStatus.OK)
async def get_all_user_devices(
        user_id: UUID = Depends(get_user_id),
        get_all_devices_use_case: GetDevicesUseCase = Depends(get_devices_get_use_case)
):
    devices = await get_all_devices_use_case.execute(user_id=user_id)
    return [ResponseDevice(**device.model_dump()) for device in devices]


@router.get("/{device_id}", response_model=ResponseDevice, status_code=http.HTTPStatus.CREATED)
async def get_device(
        device_id: UUID,
        user_id: UUID = Depends(get_user_id),
        get_single_device_use_case: GetSingleDeviceUseCase = Depends(get_single_get_use_case),
):
    device = await get_single_device_use_case.execute(device_id=device_id, user_id=user_id)
    return ResponseDevice(**device.model_dump())


@router.put("/{device_id}")
async def edit_device(
        device: EditDeviceInput, 
        device_id: UUID,
        user_id: UUID = Depends(get_user_id),
        edit_device_use_case: UpdateDeviceUseCase = Depends(get_edit_device_use_case),):
    await edit_device_use_case.execute(device_id=device_id, user_id=user_id, device=EditDeviceInput(**device.model_dump()))
    return Response(status_code=http.HTTPStatus.OK)



@router.delete("/{device_id}")
async def delete_device(
        device_id: UUID,
        user_id: UUID = Depends(get_user_id),
        delete_device_use_case: DeleteDeviceUseCase = Depends(get_devices_get_use_case),
):
    await delete_device_use_case.execute(device_id=device_id, user_id=user_id)
    return Response(status_code=http.HTTPStatus.NO_CONTENT)


@router.post("/{device_id}/execute")
async def execute_command_on_device(
        device_id: UUID,
        user_id: UUID = Depends(get_user_id),
        execute_command_use_case: ExecuteCommandUseCase = Depends(get_device_register_use_case),
):
    await execute_command_use_case.execute(device_id=device_id, user_id=user_id)
    return Response(status_code=http.HTTPStatus.OK)
