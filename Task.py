class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task(description={self.description}, due_date={self.due_date}, completed={self.completed})"

def add_task(task_list, task):
    task_list.append(task)

def get_current_tasks(task_list):
    return [task for task in task_list if not task.completed]


