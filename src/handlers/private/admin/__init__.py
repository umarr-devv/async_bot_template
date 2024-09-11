from aiogram import Router

from src.filters.chat import AdminFilter

router = Router()

router.message.filter(AdminFilter())
router.callback_query.filter(AdminFilter())
