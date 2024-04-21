from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import db

def home_keyboard():
    keyboard = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("Vazifalarim"),
                KeyboardButton("Vazifa qo'shish")
            ],
        ],
        resize_keyboard=True
    )
    return keyboard

def tasks_keyboard(user_id):
    tasks=db.get_all_tasks(user_id)
    buttons=[]
    for i in tasks:
        text = "🕔  "+i["title"]
        if i["completed"]:
            text = "✅  "+i["title"]
        buttons.append([InlineKeyboardButton(text=text, callback_data=f"task_id:{i.doc_id}")])
    return InlineKeyboardMarkup(buttons)

def task_keyboard(task_id):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="❌ bekor qilish",callback_data=f"remove:{task_id}"),
                InlineKeyboardButton(text="✅ bajarildi",callback_data=f"done:{task_id}")
            ]
        ]
    )
