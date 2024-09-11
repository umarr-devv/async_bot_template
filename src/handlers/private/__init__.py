from aiogram import Router

from src.handlers.private.user import router as user_router

router = Router()

router.include_router(user_router)
