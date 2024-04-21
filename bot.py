from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler, CallbackContext
from telegram import Update
from config import TOKEN
import handlers
import db

# Define conversation states
START, ASK_QUESTION1, ASK_QUESTION2, ASK_QUESTION3 = range(4)

data = {}

def start(update: Update, context: CallbackContext) -> int:
    data["user_id"] = update.message.chat_id
    update.message.reply_text("Vazifangiz uchun sarlavha kiriting")
    return ASK_QUESTION1

def ask_question1(update: Update, context: CallbackContext) -> int:
    data["title"] = update.message.text
    update.message.reply_text("Vazifa haqida izoh qo'shing")
    return ASK_QUESTION2

def ask_question2(update: Update, context: CallbackContext) -> int:
    data["description"] = update.message.text
    update.message.reply_text("Bajarish muhlatini belgilang (yyyy-mm-dd)")
    return ASK_QUESTION3

def ask_question3(update: Update, context: CallbackContext) -> int:
    data["until"] = update.message.text
    # Process the collected data
    print("Data:", data)
    data["added_time"]=db.time_now()
    db.add_task_db(data)
    update.message.reply_text("Vazifa muvaffaqiyatli saqlandi!")
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & Filters.regex(r"^Vazifa qo'shish$"), start)],
        states={
            ASK_QUESTION1: [MessageHandler(Filters.text & ~Filters.command, ask_question1)],
            ASK_QUESTION2: [MessageHandler(Filters.text & ~Filters.command, ask_question2)],
            ASK_QUESTION3: [MessageHandler(Filters.text & ~Filters.command, ask_question3)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(CommandHandler("start", handlers.start_home))
    dispatcher.add_handler(MessageHandler(Filters.regex(r"^Vazifalarim$"), handlers.tasks))  # Assuming tasks function is defined
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CallbackQueryHandler(handlers.task))
    # Add more handlers as needed, e.g., CallbackQueryHandler

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()