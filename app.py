import asyncio

import pytz
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.config import Config
from src.handlers import router
from src.service.database import DataBase
from src.utils.commands import set_commands
from src.utils.logs import set_logging
from src.models import Base

CONFIG_FILE = 'local-config.yml'

config = Config.create(config_file=CONFIG_FILE)
dp = Dispatcher(storage=RedisStorage.from_url(config.redis.url))
database = DataBase(config)
bot = Bot(token=config.bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
scheduler = AsyncIOScheduler(timezone=pytz.timezone('UTC'))


async def main():
    set_logging(config)
    await set_commands(bot)

    dp.include_router(router)

    try:
        scheduler.start()
        await dp.start_polling(bot, config=config,
                               sessions=database.sessions, scheduler=scheduler)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
