#yes

from aiogram import Router, types
from aiogram.types import CallbackQuery

callback_router = Router()

@callback_router.callback_query()
async def handle_callback(query: CallbackQuery):
    await query.answer("Обработка callback-запроса")