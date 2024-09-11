from aiogram import Router

from filters.chat_type import ChannelTypeFilter

router = Router()

router.message.filter(ChannelTypeFilter())
router.callback_query.filter(ChannelTypeFilter())
