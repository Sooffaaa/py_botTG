import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла
load_dotenv("dev.env")

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Получаем список владельцев бота
try:
    BOT_OWNERS = [int(x.strip()) for x in os.getenv("BOT_OWNERS", "").split(",") if x.strip()]
except ValueError as ex:
    print("Ошибка при чтении BOT_OWNERS:", ex)
    BOT_OWNERS = []

# Проверка на отсутствие токена
if not BOT_TOKEN:
    raise RuntimeError("❌ Переменная окружения BOT_TOKEN не установлена!")