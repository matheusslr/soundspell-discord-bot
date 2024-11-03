from strategies.base_command import CommandStrategy
from utils.decorators import command


@command("disconnect")
class DisconnectCommand(CommandStrategy):
    async def execute(self, message, args):
        if message.guild.voice_client and message.guild.voice_client.is_connected():
            await message.guild.voice_client.disconnect()
