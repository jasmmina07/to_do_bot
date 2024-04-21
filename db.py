from tinydb import TinyDB, Query
from pprint import*
from datetime import*

db = TinyDB("db.json", indent=4)
q=Query()

def get_all_tasks():
    tasks = db.table("tasks").all()
    return tasks

def get_task_by_doc_id(id):
    task = db.table("tasks").get(doc_id=id)
    return task

def add_task_db(data):
    task = db.table("tasks")
    task.insert(
        {
            "title" : data["title"],
            "description" : data["description"],
            "until" : data["until"],
            "added_time" : data["added_time"],
            "user_id" : data["user_id"]
        }
    )

def time_now():
    now = datetime.now()
    return str(now)


