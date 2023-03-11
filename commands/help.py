from configs.logs import logging


logger = logging.getLogger(__name__)


def help(update, context):
    """Логика команды help"""
    if update.effective_chat is not None:
        chat = update.effective_chat
        message = (
            '<em><b>Команда course</b></em>:\n'
            'После ввода команды следующим параметром '
            'введите <u>код валюты</u>\n'
            '\n<em><b>Команда sub</b></em>:\n'
            'После ввода команды нужно ввести 2 параметра, '
            '<u>время(в секундах)</u> и <u>код валюты</u>\n'
            '\n<em><b>Команда unsub</b></em>:\n'
            'Если вы хотите отписаться от рассылки,то '
            'используйте эту команду'
        )
        context.bot.send_message(
            chat_id=chat.id,
            text=message,
            parse_mode='html'
        )
    else:
        logger.warning('Не получен id чата "/help"')
