from telegram.ext import Updater, CommandHandler
from config import TOKEN
from handlers import*


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start",start))

    updater.start_polling()
    updater.idle()


if __name__=="__main__":
    main()