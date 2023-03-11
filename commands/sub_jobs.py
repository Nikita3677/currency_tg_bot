from configs.logs import logging
from configs import constants
from utils import hand
from datetime import datetime

logger = logging.getLogger(__name__)


def remove_job(name, context):
    jobs = context.job_queue.get_jobs_by_name(name)
    if not jobs:
        return False
    for job in jobs:
        job.schedule_removal()
    return True


def new_course(context):
    """Логика команды new_course"""
    try:
        job = context.job
        valute_code = context.bot_data['name'].upper()
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
        context.bot.send_message(job.context, text=message)
    except Exception:
        message = 'Такой валюты нет !'
        context.bot.send_message(job.context, text=message)
        logger.warning('Неправильный код валюты пропускаем')


def sub(update, context):
    if update.effective_chat is not None:
        chat = update.effective_chat
        try:
            time = int(context.args[0])
            if time <= 0:
                update.message.reply_text('Время должно быть больше нуля!')
                logger.warning('Ввели отрицательное время')
                return
            valute_code = context.args[1].upper()
            context.bot_data['name'] = valute_code
            response = hand.make_request(constants.URL).json()
            response_val = response.get('Valute')
            if valute_code not in response_val:
                update.message.reply_text('Такой валюты нет!')
                logger.warning('Неправильный код валюты пропускаем')
                return
            job_remove = remove_job(str(chat.id), context)
            context.job_queue.run_repeating(
                new_course, time,
                context=chat.id, name=str(chat.id)
            )
            message = "Вы подписались на новую рассылку"
            if job_remove:
                message += " и удалили старую"
            update.message.reply_text(message)
        except Exception as er:
            update.message.reply_text('Неверно введены данные')
            logger.warning(f'Валидация данных "/sub", ошибка: {er}')
    else:
        logger.warning('Не получен id чата "/sub"')


def unsub(update, context):
    if update.effective_chat is not None:
        chat = update.effective_chat
        job_remove = remove_job(str(chat.id), context)
        message = 'Рассылка отменена' if job_remove else 'Нет активных рассылок'
        update.message.reply_text(message)
    else:
        logger.warning('Не получен id чата "/unsub"')
