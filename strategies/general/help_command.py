import discord
from utils.command_context import command_context
from strategies.base_command import CommandStrategy
from utils.decorators import command

@command("help")
class HelpCommand(CommandStrategy):
    async def execute(self, message: discord.Message, args: list[str]):
        commands_list = ", ".join(f"!{cmd}" for cmd in command_context.strategies.keys())
        help_message = f"Comandos disponíveis: {commands_list}"
        await message.channel.send(help_message)
