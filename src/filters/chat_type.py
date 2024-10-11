from aiogram import types
from aiogram.enums.chat_type import ChatType
from aiogram.filters import BaseFilter


class ChatTypeFilter(BaseFilter):
    chat_types: list[str] = []

    async def __call__(self, get: types.Message | types.CallbackQuery) -> bool:
        if isinstance(get, types.CallbackQuery):
            get = get.message
        return get.chat.type in self.chat_types


class PrivateTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.PRIVATE]


class GroupTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.GROUP, ChatType.SUPERGROUP]


class ChannelTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.CHANNEL]
