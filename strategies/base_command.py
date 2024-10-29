import discord
from abc import ABC, abstractmethod

class CommandStrategy(ABC):
    @abstractmethod
    async def execute(self, message: discord.Message, args: list[str]):
        pass
