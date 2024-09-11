import asyncio
import sys

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import Config
from src.service.database import DataBase
from src.utils.logs import set_logging
from src.handlers import router


async def main():
    config_file = sys.argv[1]
    config = Config.create(config_file=config_file)

    set_logging(config=config)

    dp = Dispatcher(storage=MemoryStorage())
    database = DataBase(config=config)
    bot = Bot(token=config.bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.include_router(router)

    try:
        await dp.start_polling(bot, database=database, config=config)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
