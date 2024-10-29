import discord
import random
from strategies.base_command import CommandStrategy
from utils.decorators import command


@command("roll")
class RollDiceCommand(CommandStrategy):
    async def execute(self, message: discord.Message, args: list[str]):
        if (len(args) < 1):
            await message.channel.send("Informe o número de dados a serem rolados. Exemplo: !roll 2d6")
            return
        
        dice = args[0].split("d")
        if (len(dice) != 2):
            await message.channel.send("Formato inválido. Use !roll <quantidade>d<lados>")
            return
        if (not dice[0].isdigit() or not dice[1].isdigit()):
            await message.channel.send("Formato inválido. Use !roll <quantidade>d<lados>")
            return
        
        await message.channel.send("Rolando os dados...")

        quantity = int(dice[0])
        sides = int(dice[1])
        results = [random.randint(1, sides) for _ in range(quantity)]

        await message.channel.send(f"Resultado: {', '.join(str(r) for r in results)}")
        await message.channel.send(f"Soma: {sum(results)}")