from strategies.base_command import CommandStrategy
from utils.decorators import command


@command("clear")
class ClearCommand(CommandStrategy):
    async def execute(self, message, args):
        if not message.author.guild_permissions.administrator:
            await message.channel.send("Você não tem permissão para usar esse comando.")
            return
        await message.channel.purge()
        await message.channel.send("Mensagens apagadas com sucesso.")