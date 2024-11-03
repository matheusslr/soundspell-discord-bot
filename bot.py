import discord
import importlib
import os
from dotenv import load_dotenv
from utils.command_context import command_context

command_modules = [
    'strategies.general.help_command',
    'strategies.general.sound.play_command',
    'strategies.general.disconnect_command',
    'strategies.rpg.roll_dice',
    'strategies.admin.clear_command'
]

for module in command_modules:
    importlib.import_module(module)

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        parts = message.content.strip().split(" ")
        command_name = parts[0][1:]
        args = parts[1:]

        await command_context.execute_strategy(command_name, message, args)

client.run(BOT_TOKEN)
