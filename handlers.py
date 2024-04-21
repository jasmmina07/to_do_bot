from telegram import Update
from telegram.ext import CallbackContext
from keyboards import*
from pprint import pprint
import db


def start_home(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text="""Assalomu aleykum! Botimizga xush kelibsiz. O'z mashg'ulot jadvalingizni yaratish uchun ro'yxatdan o'tish tugmasini bosing!"""

    update.message.reply_text(
        text=text,
        reply_markup=home_keyboard()
    )
    print("/start")

def tasks(update: Update,context: CallbackContext):
    update.message.reply_text(
        text="Vazifalarim:",
        reply_markup=tasks_keyboard()
    )

def task(update: Update, context: CallbackContext):
    a,id=update.callback_query.data.split(":")
    task=db.get_task_by_doc_id(id)
    text=text=f"""
            Vazifa: {task["title"]}
            
📌{task["description"]}, 
⏳{task["until"]} gacha


{task["added_time"]}

            """

    update.callback_query.edit_message_text(
        text=text
    )
    update.callback_query.edit_message_reply_markup(
        reply_markup=task_keyboard(id)
    )


