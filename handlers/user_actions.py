from aiogram import Router, types

user_router = Router()

# Пример обработчика сообщений от пользователей в группах
# @user_router.message()
# async def handle_user_message(message: types.Message):
#     if message.chat.type in ["group", "supergroup"]:
#         # Добавь сюда нужную логику
#         await message.reply("Принято! Вы написали в группе.")