import logging
import json
from datetime import datetime 

logger = logging.getLogger(__name__)

TEXT = "INSERT ONE COMMAND\n- Add(id:int)\n- UPDATE(id:int)\nDELETE(id:int)\n- STATUS(progress-finish)\n- LIST(done - todo - in-progress)\n\n"
PATH_BD = "./db/db.json"



def main():
    logging.basicConfig(filename='tasks_tracker.log', level=logging.INFO)
    print("TASK TRACKER")
    
    db = None 
    try:
        with open(PATH_BD) as f:
            db = json.load(f)
    except Exception as e:
        logging.error(msg=f"NO DB: {str(e)}")
    
    breakpoint = True 
    if db is not None:
        while breakpoint:
            command = str(input(TEXT)).split(" ")

            if command[0].lower() == "add" and len(command) == 2:
                print("ADD TASK\n")
                task = command[1]  
                if len(db) > 0:
                    last_id = db[-1]["id"] +1 
                else:
                    last_id = 1
                task = {"id": last_id, "description": task, "status": "not-done", "createdAt": str(datetime.now()), "updatedAt": None}
                db.append(task)
                print(f"\nTASK CREATED: {task}")
                with open(PATH_BD, 'w') as f:
                    json.dump(db, f)

            if command[0].lower() == "update" and len(command) == 3:
                print("UPDATE\n")
                for task_tmp in db:
                    if task_tmp["id"] == int(command[1]):
                        task_tmp["description"] = command[2]
                        task_tmp["updatedAt"] = str(datetime.now())
                        print(f"\nTASK UPDATED: {task_tmp}\n")
                        with open(PATH_BD, 'w') as f:
                            json.dump(db, f)
            
            if command[0].lower() == "delete" and len(command) == 2:
                print("DELETE\n")
                for index, task_tmp in enumerate(db):
                    if task_tmp["id"] == int(command[1]):
                        print(f"\nTASK DELETE: {task_tmp}\n")
                        del db[index]
                    with open(PATH_BD, 'w') as f:
                        json.dump(db, f) 

            if command[0].lower() == "mark-in-progress" and len(command) == 2:
                print("MARK IN PROGRESS\n")
                for task_tmp in db:
                    if task_tmp["id"] == int(command[1]):
                        task_tmp["status"] = "in-progress"
                        task_tmp["updatedAt"] = str(datetime.now())
                        print(f"\nTASK UPDATED: {task_tmp}\n" )
                        with open(PATH_BD, 'w') as f:
                            json.dump(db, f)
            
            if command[0].lower() == "mark-done" and len(command) == 2:
                print("MARK DONE TASK\n")
                for task_tmp in db:
                    if task_tmp["id"] == int(command[1]):
                        task_tmp["status"] = "done"
                        task_tmp["updatedAt"] = str(datetime.now())
                        print(f"\nTASK UPDATED: {task_tmp}\n" )
                        with open(PATH_BD, 'w') as f:
                            json.dump(db, f)

            if command[0].lower() == "list" and len(command) == 1:
                print("LIST ALL TASKS: \n")
                for task in db:
                    print(task, "\n")

            if command[0].lower() == "list" and len(command) == 2 and command[1] == "done":
                print("LIST TASKS(DONE)\n")
                for task in db:
                    if task["status"] == "done":
                        print(task, "\n")

            if command[0].lower() == "list" and len(command) == 2 and command[1] == "todo":
                print("LIST TASKS(TODO)\n")
                for task in db:
                    if task["status"] == "not-done":
                        print(task, "\n")


            if command[0].lower() == "list" and len(command) == 2 and command[1] == "in-progress":
                print("LIST TASKS(IN-PROGRESS)\n")
                for task in db:
                    if task["status"] == "in-progress":
                        print(task, "\n")



            if command[0].lower() == "exit": 
                breakpoint = False




if __name__ == "__main__":
    main()