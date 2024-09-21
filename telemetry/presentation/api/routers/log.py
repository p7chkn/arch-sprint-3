import http

from fastapi import APIRouter, Depends, Response
from uuid import UUID

from application.log.usecases.log import GetLogsUseCase, GetDeviceStatusUseCase
from presentation.dependencies.log import get_logs_use_case, get_device_status_use_case

from presentation.api.routers.schemas.logs import LogResponse

router = APIRouter(
    prefix="",
)

@router.get("/{device_id}", response_model=list[LogResponse], status_code=http.HTTPStatus.OK)
async def get_logs(
        device_id: UUID,
        get_log_use_case: GetLogsUseCase = Depends(get_logs_use_case),
):
    logs = await get_log_use_case.execute(device_id=device_id)
    return [LogResponse(**log.model_dump()) for log in logs]


@router.get("/{device_id}/status", response_model=LogResponse, status_code=http.HTTPStatus.OK)
async def edit_device(
        device_id: UUID,
        get_devise_status_use_case: GetDeviceStatusUseCase = Depends(get_device_status_use_case),):
    log = await get_devise_status_use_case.execute(device_id=device_id)
    if not log:
        return Response(status_code=http.HTTPStatus.NOT_FOUND)
    return LogResponse(**log.model_dump())
