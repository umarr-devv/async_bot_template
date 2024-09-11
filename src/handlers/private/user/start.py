from aiogram import types, Router
from aiogram.filters import CommandStart, CommandObject

from src.models.crud import create_user
from src.service.database import DataBase

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject):
    text = f'Добро пожаловать, {message.from_user.full_name}'
    await message.answer(text=text)
