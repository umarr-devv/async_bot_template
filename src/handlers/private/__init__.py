from aiogram import Router

from src.filters.chat_type import PrivateTypeFilter
from src.handlers.private.admin import router as admin_router
from src.handlers.private.user import router as user_router

router = Router()

router.include_router(admin_router)
router.include_router(user_router)

router.message.filter(PrivateTypeFilter())
router.callback_query.filter(PrivateTypeFilter())
