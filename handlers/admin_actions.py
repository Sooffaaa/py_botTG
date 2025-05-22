# yes

from aiogram import Router, types
from aiogram.filters import Command
from filters import IsAdminFilter

admin_router = Router()

@admin_router.message(Command("ban"), IsAdminFilter())
async def ban_command_handler(message: types.Message):
    await message.reply("Команда /ban получена. Здесь будет логика блокировки.")