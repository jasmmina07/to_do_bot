from tinydb import TinyDB, Query
from pprint import*
from datetime import*

db = TinyDB("db.json", indent=4)
item = Query()

def get_all_tasks(user_id):
    tasks = db.table("tasks").search(item.user_id==user_id)
    print(tasks)
    return tasks

def get_task_by_doc_id(id):
    task = db.table("tasks").get(doc_id=id)
    return task

def add_task_db(data):
    table = db.table("tasks")
    table.insert(
        {
            "title" :       data["title"],
            "description" : data["description"],
            "until" :       data["until"],
            "added_time" :  data["added_time"],
            "user_id" :     data["user_id"],
            "completed":    data["completed"]
        }
    )

def time_now():
    now = datetime.now()
    return str(now)

def delete_task_db(id):
    table = db.table("tasks")
    table.remove(doc_ids=[id])

def done_task_db(id):
    table = db.table("tasks")
    data = table.get(doc_id=id)
    # data=dict(item)
    data["completed"]=True
    task=table.get(doc_id=id)
    task.update(data)
    table.update(task, doc_ids=[id])

