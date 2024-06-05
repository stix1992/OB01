class Task:
    def __init__(self):
        self.task_list = []

    def add_task(self, description, due_date):
        self.task_list.append({'description':description, 'due_date':due_date, 'completed':False})
        print(f'Задача "{description}" добавлена!')

    def mark_completed(self, description):
        for task in self.task_list:
            if task['description'] == description:
                task['completed'] = True
                print(f'Задача "{description}" выполнена!')
                break
        else:
            print(f'Задача "{description}" не найдена!')

    def __str__(self):
        return '\nCписок задач:\n' + '\n'.join([f'   {task["description"]} - выполнить до {task["due_date"]}' for task in self.task_list if not task['completed']])


