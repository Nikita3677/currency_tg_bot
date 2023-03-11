from configs.logs import logging


logger = logging.getLogger(__name__)


def commands(update, context):
    """Логика команды commands"""
    if update.effective_chat is not None:
        chat = update.effective_chat
        message = (
            f'=======<b>Список команд</b>========\n'
            f'\n~ /show_all - курс популярных валют\n'
            f'\n~ /course - курс интересующей валюты\n'
            f'\n~ /sub - подписаться на рассылку\n'
            f'\n~ /unsub - отписаться от рассылки\n'
            f'\n~ /help - как пользоваться\n'
            f'\n~ /start - приветственная информация\n'
        )
        context.bot.send_message(chat_id=chat.id, text=message, parse_mode='html')
    else:
        logger.warning('Не получен id чата "/commands"')