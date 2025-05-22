# yes

from aiogram import Router, types

group_router = Router()

@group_router.message(content_types=["new_chat_members", "left_chat_member"])
async def on_user_join_or_left(message: types.Message):
    """
    Удаляет сообщения о входе/выходе участников.
    """
    await message.delete()