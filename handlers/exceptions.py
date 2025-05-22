# yes

import logging
from aiogram import Dispatcher
from aiogram.types import Update
from aiogram.exceptions import (
    TelegramAPIError, CantDemoteChatCreator, MessageNotModified,
    MessageToDeleteNotFound, MessageTextIsEmpty, RetryAfter,
    CantParseEntities, MessageCantBeDeleted, Unauthorized, InvalidQueryID
)

# Основной хендлер ошибок
async def global_error_handler(update: Update, exception: Exception) -> None:
    if isinstance(exception, CantDemoteChatCreator):
        logging.debug("Can't demote chat creator")
    elif isinstance(exception, MessageNotModified):
        logging.debug("Message is not modified")
    elif isinstance(exception, MessageCantBeDeleted):
        logging.debug("Message can't be deleted")
    elif isinstance(exception, MessageToDeleteNotFound):
        logging.debug("Message to delete not found")
    elif isinstance(exception, MessageTextIsEmpty):
        logging.debug("Message text is empty")
    elif isinstance(exception, Unauthorized):
        logging.info(f"Unauthorized: {exception}")
    elif isinstance(exception, InvalidQueryID):
        logging.exception(f"InvalidQueryID: {exception}\nUpdate: {update}")
    elif isinstance(exception, RetryAfter):
        logging.warning(f"RetryAfter: {exception}\nUpdate: {update}")
    elif isinstance(exception, CantParseEntities):
        logging.exception(f"CantParseEntities: {exception}\nUpdate: {update}")
    elif isinstance(exception, TelegramAPIError):
        logging.exception(f"TelegramAPIError: {exception}\nUpdate: {update}")
    else:
        logging.exception(f"Unhandled exception: {exception}\nUpdate: {update}")