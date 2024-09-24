from uuid import UUID

from application.device.models.device import CommandInput
from application.device.usecases.interfaces import DeviceCommandExecuteRepoInterface


class MockDeviceCommandExecutor(DeviceCommandExecuteRepoInterface):
    async def execute_command(self, device_id: UUID,
                              user_id: UUID, commands: list[CommandInput]):
        for command in commands:
            print(f"pretending to execute command {command} for user {user_id} on device {device_id}")