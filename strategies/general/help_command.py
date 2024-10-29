from strategies.base_command import CommandStrategy
import discord
from utils.decorators import command

@command("help")
class HelpCommand(CommandStrategy):
    async def execute(self, message: discord.Message, args: list[str]):
        await message.channel.send("Hello!")
