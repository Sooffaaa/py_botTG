# from aiogram import types
# from aiogram.dispatcher.filters import BoundFilter
# import config


# class IsOwnerFilter(BoundFilter):
#     """
#     Custom filter "is_owner".
#     """
#     key = "is_owner"

#     def __init__(self, is_owner):
#         self.is_owner = is_owner

#     async def check(self, message: types.Message):
#         return message.from_user.id in config.BOT_OWNERS


# class IsAdminFilter(BoundFilter):
#     """
#     Filter that checks for admin rights existence
#     """
#     key = "is_admin"

#     def __init__(self, is_admin: bool):
#         self.is_admin = is_admin

#     async def check(self, message: types.Message):
#         member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
#         return member.is_chat_admin() == self.is_admin


# class MemberCanRestrictFilter(BoundFilter):
#     """
#     Filter that checks member ability for restricting
#     """
#     key = 'member_can_restrict'

#     def __init__(self, member_can_restrict: bool):
#         self.member_can_restrict = member_can_restrict

#     async def check(self, message: types.Message):
#         member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)

#         # I don't know why, but telegram thinks, if member is chat creator, he cant restrict member
#         return (member.is_chat_creator() or member.can_restrict_members) == self.member_can_restrict


from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import BaseFilter
from config import BOT_OWNERS


class IsOwnerFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in BOT_OWNERS


class IsAdminFilter(BaseFilter):
    def __init__(self, is_admin: bool = True):
        self.is_admin = is_admin

    async def __call__(self, message: Message, bot: Bot) -> bool:
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin() == self.is_admin


class MemberCanRestrictFilter(BaseFilter):
    def __init__(self, member_can_restrict: bool = True):
        self.member_can_restrict = member_can_restrict

    async def __call__(self, message: Message, bot: Bot) -> bool:
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        return (member.is_chat_creator() or member.can_restrict_members) == self.member_can_restrict
