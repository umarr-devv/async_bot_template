import asyncio
import sys

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import Config


async def main():
    config_file = sys.argv[1]
    config = Config.create(config_file=config_file)

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=config.bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    try:
        await dp.start_polling(bot=bot, config=config)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
