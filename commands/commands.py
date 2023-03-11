from configs.logs import logging


logger = logging.getLogger(__name__)


def commands(update, context):
    """Логика команды commands"""
    if update.effective_chat is not None:
        chat = update.effective_chat
        message = (
            '=======<b>Список команд</b>========\n'
            '\n~ /show_all - курс популярных валют\n'
            '\n~ /course - курс интересующей валюты\n'
            '\n~ /sub - подписаться на рассылку\n'
            '\n~ /unsub - отписаться от рассылки\n'
            '\n~ /help - как пользоваться\n'
            '\n~ /start - приветственная информация\n'
        )
        context.bot.send_message(
            chat_id=chat.id,
            text=message,
            parse_mode='html'
        )
    else:
        logger.warning('Не получен id чата "/commands"')
