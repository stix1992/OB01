class Task:
    def __init__(self, description, due_date, task_list):
        self.description = description
        self.due_date = due_date
        self.completed = False
        task_list.append(self)
        print(f'Задача "{self.description}" добавлена!')

    def mark_completed(self):
        self.completed = True
        print(f'Задача "{self.description}" выполнена!')

    def __str__(self):
        return f"{self.description} - выполнить до {self.due_date}"

def get_current_tasks(task_list):
    return [task for task in task_list if not task.completed]

