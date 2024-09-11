from aiogram import Router

from filters.chat_type import GroupTypeFilter

router = Router()

router.message.filter(GroupTypeFilter())
router.callback_query.filter(GroupTypeFilter())
