# Define the Task class to represent a to-do item
class Task:
    def _init_(self, title):
        self.title = title
        self.completed = False

    def _str_(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.title} - {status}"

# Define the ToDoList class to manage a list of tasks
class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Here are your tasks:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def update_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = not task.completed
            status = "completed" if task.completed else "incomplete"
            print(f"Task '{task.title}' marked as {status}.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.title}' deleted.")
        else:
            print("Invalid task number.")

# Command-line interface
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task (Mark as Complete/Incomplete)")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice from (1-5): ")

        if choice == "1":
            title = input("Enter the task title: ")
            todo_list.add_task(title)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            todo_list.update_task(task_number)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Goodbye! Have a nice day")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if _name_ == "_main_":
    main()