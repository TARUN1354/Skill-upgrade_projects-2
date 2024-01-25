class Task:
    def __init__(self, description, is_complete=False):
        self.description = description
        self.is_complete = is_complete

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].is_complete = True

    def view_list(self):
        for i, task in enumerate(self.tasks):
            status = '[X]' if task.is_complete else '[ ]'
            print(f"{i+1}. {status} {task.description}")

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n1. Add task\n2. Mark complete\n3. View list\n4. Quit")
        option = int(input("Choose an option: "))
        if option == 1:
            todo_list.add_task(input("Enter a task: "))
        elif option == 2:
            todo_list.view_list()
            todo_list.mark_complete(int(input("Enter the task number to mark as complete: "))-1)
        elif option == 3:
            todo_list.view_list()
        elif option == 4:
            break
        else:
            print("Invalid option, try again.")
