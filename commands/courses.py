from configs.logs import logging
from configs import constants
from utils import hand
from datetime import datetime


logger = logging.getLogger(__name__)


def show_all(update, context):
    """Логика команды show_all"""
    if update.effective_chat is not None:
        chat = update.effective_chat
        response = hand.make_request(constants.URL).json()
        courses_date = datetime.strptime(
                response['Timestamp'], '%Y-%m-%dT%H:%M:%S%z',
            ).strftime('%d %B, %H:%M')
        response_val = response.get('Valute')
        valutes = constants.VALUTES
        values_valutes = {}
        for valute in valutes:
            values_valutes[valute] = response_val.get(valute).get('Value')
        message = (
            f'<b>Курсы валют на момент: {courses_date}</b>\n'
            f'Доллар - {values_valutes.get("USD")}\n'
            f'Евро - {values_valutes.get("EUR")}\n'
            f'Фунт - {values_valutes.get("GBP")}\n'
            f'Дирхам - {values_valutes.get("AED")}\n'
        )
        context.bot.send_message(chat_id=chat.id, text=message, parse_mode='html')
    else:
        logger.warning('Не получен id чата "/show_all"')


def course(update, context):
    """Логика команды course"""
    if update.effective_chat is not None:
        try:
            chat = update.effective_chat
            name = update.message.chat.first_name
            valute_code = context.args[0].upper()
            response = hand.make_request(constants.URL).json()
            courses_date = datetime.strptime(
                response['Timestamp'], '%Y-%m-%dT%H:%M:%S%z',
            ).strftime('%d %B, %H:%M')
            response_val = response.get('Valute')
            valute = response_val.get(valute_code)
            value = valute.get('Value')
            nominal = valute.get('Nominal')
            valute_name = valute.get('Name')
            message = (
                f'Курс "{valute_name}" к рублю: {value}.\n'
                f'Дата и время: {courses_date}'
            )
            if nominal > 1:
                message += f'\n В соотношении 1 RUB к {nominal} {valute_code}'
            context.bot.send_message(chat_id=chat.id, text=message)
        except Exception:
            message = f'{name}, а вы верно ввели код валюты ?'
            context.bot.send_message(chat_id=chat.id, text=message)
            logger.warning('Неправильный код валюты пропускаем')
    else:
        logger.warning('Не получен id чата "/course"')