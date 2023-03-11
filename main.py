import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from commands import commands, courses, help, start, sub_jobs

load_dotenv()
TG_TOKEN = os.getenv('TG_BOT_TOKEN')


def main():
    try:
        updater = Updater(token=TG_TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler('start', start.start))
        dispatcher.add_handler(CommandHandler('commands', commands.commands))
        dispatcher.add_handler(CommandHandler('show_all', courses.show_all))
        dispatcher.add_handler(CommandHandler('course', courses.course))
        dispatcher.add_handler(CommandHandler('sub', sub_jobs.sub))
        dispatcher.add_handler(CommandHandler('unsub', sub_jobs.unsub))
        dispatcher.add_handler(CommandHandler('help', help.help))
        updater.start_polling()
        updater.idle()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
