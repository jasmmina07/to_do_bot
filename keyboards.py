from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import db

def home_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton("Vazifalarim"),KeyboardButton("Vazifa qo'shish")]],resize_keyboard=True)

def tasks_keyboard():
    tasks=db.get_all_tasks()
    buttons=[]
    for i in tasks:
        buttons.append([InlineKeyboardButton(text=i["title"], callback_data=f"task_id:{i.doc_id}")])
    return InlineKeyboardMarkup(buttons)

def task_keyboard(task_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="❌Bekor qilish",callback_data="Vazifalarim"),
                InlineKeyboardButton(text="✅ bajarildi",callback_data=f"task_id:{task_id}")
            ]
        ]
    )
