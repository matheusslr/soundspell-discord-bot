from strategies.base_command import CommandStrategy

class CommandContext:
    def __init__(self):
        self.strategies = {}

    def register_strategy(self, name: str, strategy_class):
        self.strategies[name] = strategy_class

    async def execute_strategy(self, command_name: str, message, args):
        strategy_class = self.strategies.get(command_name)
        if strategy_class:
            strategy_instance = strategy_class()
            await strategy_instance.execute(message, args)
        else:
            await message.channel.send("Comando não reconhecido! Use !help para ver os comandos disponíveis.")

command_context = CommandContext()
