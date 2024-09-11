from aiogram import Router

from src.handlers.private import router as private_router

router = Router()

router.include_router(private_router)
