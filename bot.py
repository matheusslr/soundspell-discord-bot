import discord
import os
from dotenv import load_dotenv
from command_context import command_context
from strategies.general.help_command import HelpCommand
from strategies.rpg.roll_dice import RollDiceCommand

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        parts = message.content.strip().split(" ")
        command_name = parts[0][1:]
        args = parts[1:]

        await command_context.execute_strategy(command_name, message, args)

client.run(BOT_TOKEN)
