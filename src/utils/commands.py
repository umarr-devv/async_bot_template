from aiogram import types, Bot

COMMANDS = [
    types.BotCommand(
        command='start',
        description='Запустить бота'
    ),
    types.BotCommand(
        command='help',
        description='Помощь'
    )
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        commands=COMMANDS,
        scope=types.BotCommandScopeAllPrivateChats()
    )
