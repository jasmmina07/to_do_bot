from telegram import Update
from telegram.ext import CallbackContext
from keyboards import*
from pprint import pprint
import db


def start_home(update: Update, context: CallbackContext):
    text="""Assalomu aleykum!

Botimizga xush kelibsiz. O'z mashg'ulot jadvalingizni yaratishda ushbu bot sizga yordamchi bo'ladi deb umid qilamiz!"""

    update.message.reply_text(
        text=text,
        reply_markup=home_keyboard()
    )
    print("/start")

def tasks(update: Update,context: CallbackContext):
    user_id=update.message.chat_id
    update.message.reply_text(
        text="Vazifalarim:",
        reply_markup=tasks_keyboard(user_id)
    )

def task(update: Update, context: CallbackContext):
    a,id=update.callback_query.data.split(":")
    task=db.get_task_by_doc_id(int(id))
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
        reply_markup=task_keyboard(int(id))
    )

def remove_task(update: Update, context: CallbackContext):
    a,id=update.callback_query.data.split(":")
    db.delete_task_db(int(id))

    update.callback_query.edit_message_text(
        text="Vazifa bekor qilindi 🙄"

    )

def done_task(update: Update, context: CallbackContext):
    a,id=update.callback_query.data.split(":")
    db.done_task_db(int(id))

    update.callback_query.edit_message_text(
        text="Ofarin! Vazifani bajarganingiz bilan tabriklaymiz."
    )
