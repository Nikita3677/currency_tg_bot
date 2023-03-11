from telegram import ReplyKeyboardMarkup
from configs.logs import logging


logger = logging.getLogger(__name__)


def start(update, context):
    """Логика команды start"""
    if update.effective_chat is not None:
        chat = update.effective_chat
        name = update.message.chat.first_name
        button = ReplyKeyboardMarkup([['/commands','/help','/show_all']], resize_keyboard=True)
        message = (
            f'Привет {name},\n'
            f'Я могу прислать тебе '
            f'курс интересующей тебя валюты.\n'
            f'Для того чтобы узнать, что я могу, введи:'
            f'\n/commands - это покажет список доступных команд.\n'
        )
        context.bot.send_message(chat_id=chat.id, text=message, reply_markup=button)
    else:
        logger.warning('Не получен id чата "/start"')