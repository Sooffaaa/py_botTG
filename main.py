import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from exceptions import global_error_handler

from handlers.admin import admin_router
from handlers.callbacks import callback_router
from handlers.group_events import group_router
from handlers.personal import personal_router
from handlers.user import user_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Обработка исключений
    dp.errors.register(global_error_handler)

    # Подключаем роутеры (включают фильтры напрямую в декораторах)
    dp.include_router(admin_router)
    dp.include_router(callback_router)
    dp.include_router(group_router)
    dp.include_router(personal_router)
    dp.include_router(user_router)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())