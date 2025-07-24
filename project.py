import pyfiglet
import os
import json
from datetime import date
import time
import playsound
from colorama import init, Fore, Back, Style
init(autoreset=True)

def main():
    #printing a banner
    banner = pyfiglet.figlet_format("FocusForge", font = "big", width = 100)
    print(Fore.CYAN + Style.BRIGHT + banner)

    print(Fore.YELLOW + Style.BRIGHT + "✨  Welcome to the Productivity App! Stay consistent. Stay awesome! 🚀\n")

    while True:
        print(Fore.MAGENTA + Style.BRIGHT + "\n📋  Main Menu:")
        print("Choose an option by entering the preceding number.")
        print("1. Manage To-Do List\n2. Track Habits\n3. Start Pomodoro Timer\n4. Write a Note\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Error: Invalid option. Select a number from the menu.")
            continue
        # exiting the app
        if choice == 5:
            break
        # To-Do list
        elif choice == 1:
            print(Fore.MAGENTA + Style.BRIGHT + "📝  To-Do List Options:")
            print("1. ➕  Add Task\n2. 📋  View Tasks\n3. ✅  Mark Task as Done\n4. 🗑️  Delete Task\n5. ✏️  Edit Task")
            try:
                todo_choice = int(input("Enter your choice: "))
            except ValueError:
                print(Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Error: Invalid option. Select a number from the menu.")
                continue
            if todo_choice == 1:
                print(add_task())
            elif todo_choice == 2:
                view_tasks()
            elif todo_choice == 3:
                print(mark_task_done())
            elif todo_choice == 4:
                print(delete_task())
            elif todo_choice == 5:
                print(edit_task())
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")
        # Habit tracking
        elif choice == 2:
            print(Fore.MAGENTA + Style.BRIGHT + "📈 Habit Tracking Options:")
            print("1. ➕  Track Habit\n2. 📅  View Habit History")
            try:
                habit_choice = int(input("Enter your choice: "))
            except ValueError:
                print(Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Error: Invalid option. Select a number from the menu.")
                continue
            if habit_choice == 1:
                print(add_habit())
            elif habit_choice == 2:
                view_habits()
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")
        # Pomodoro Timer
        elif choice == 3:
            start_timer()
        # Note-taking
        elif choice == 4:
            print(Fore.MAGENTA + Style.BRIGHT + "🗒️  Note Options:")
            print("1. ✍️  Add Note\n2. 📖  View Notes")
            try:
                note_choice = int(input("Enter your choice: "))
            except ValueError:
                print(Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Error: Invalid option. Select a number from the menu.")
                continue
            if note_choice == 1:
                print(add_notes())
            elif note_choice == 2:
                view_notes()
            else:
                print(Fore.RED + "❌ Invalid choice. Please try again.")
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")
    #loop ends
    print(Fore.BLUE + Style.BRIGHT + "👋  Thank you for using the Productivity App! Keep crushing your goals!  💪")


#loads data from tasks.json
def load_tasks():
    if not os.path.exists("./data/tasks.json"):
        return []
    try:
        with open("./data/tasks.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

#adds a task to tasks.json
def add_task(task=None):
    if task is None:
        task = input("Enter the task description: ")
    task = task.strip()
    if not task:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ Task description cannot be empty.")
    tasks = load_tasks()
    for list_task in tasks:
        if list_task["task"].lower() == task.lower():
            return (Fore.YELLOW + Style.RESET_ALL + "⚠️ This task already exists.")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    return (Fore.GREEN + Style.RESET_ALL + "✅ Task added successfully.")

#saves tasks to tasks.json
def save_tasks(tasks):
    with open("./data/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

#views all tasks from tasks.json
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + Style.RESET_ALL + "⚠️ No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{index}. 🗂️  {task['task']} - {status}")

#mark as done
def mark_task_done(task_number=None):
    tasks = load_tasks()
    if not tasks:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ No tasks available to mark as done.")
    view_tasks()
    try:
        if task_number is None:
            task_number = input("Enter the task number to mark as done: ")
        task_number = int(task_number) #in case user passes a string
        if 1 <= task_number <= len(tasks):
            if tasks[task_number - 1]["done"]:
                return (Fore.YELLOW + Style.RESET_ALL + "⚠️ This task is already marked as done.")
            tasks[task_number - 1]["done"] = True
            save_tasks(tasks)
            return (Fore.GREEN + Style.RESET_ALL + "✅ Task marked as done.")
        else:
            return (Fore.RED + Style.RESET_ALL + "❌ Invalid task number.")
    except ValueError:
        return (Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Invalid input: Please enter a valid task number.")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ No tasks available to delete.")
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            save_tasks(tasks)
            return (Fore.GREEN + Style.RESET_ALL + "✅ Task deleted successfully.")
        else:
            return (Fore.RED + Style.RESET_ALL + "❌ Invalid task number.")
    except ValueError:
        return (Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Invalid input: Please enter a valid task number.")

def edit_task():
    tasks = load_tasks()
    if not tasks:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ No tasks available to edit.")
    view_tasks()
    try:
        task_number = int(input("Enter the task number to edit: ").strip())
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task description: ").strip()
            if not new_task:
                return (Fore.YELLOW + Style.RESET_ALL + "⚠️ Task description cannot be empty.")
            tasks[task_number -1]["task"] = new_task
            save_tasks(tasks)
            return (Fore.GREEN + Style.RESET_ALL + "✅ Task edited successfully.")
        else:
            return (Fore.RED + Style.RESET_ALL + "❌ Invalid task number.")
    except ValueError:
        return (Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Invalid input: Please enter a valid task number.")

#load habits from habits.json
def load_habits():
    if not os.path.exists("./data/habits.json"):
        return {"habit": [], "date": []}
    try:
        with open("./data/habits.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"habit": [], "date": []}

# logic to track/add habits
def add_habit(habit = None):
    if habit is None:
        habit = input("Enter the habit you want to track: ")
    habit = habit.strip()
    if not habit:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ Habit description cannot be empty.")
    habits = load_habits()
    today = date.today().isoformat()
    if habit in habits["habit"]:
        return (Fore.YELLOW + Style.RESET_ALL + f"⚠️ You have already tracked the habit '{habit}' today.")
    habits["habit"].append(habit)
    habits["date"].append(today)
    save_habits(habits)
    return (Fore.GREEN + Style.RESET_ALL + f"✅ Habit '{habit}' tracked for today!")

#save habits to habits.json
def save_habits(habits):
    with open("./data/habits.json", "w") as file:
        json.dump(habits, file, indent=4)

#view habits from habits.json
def view_habits():
    habits = load_habits()
    if not habits["habit"]:
        return (Fore.YELLOW + Style.RESET_ALL + "⚠️ No habits tracked yet.")
    for habit, date in zip(habits["habit"], habits["date"]):
        print(f"📌 Habit: {habit} - 📅 Date: {date}")
    print(f"\n📊 Total habits tracked: {len(habits['habit'])}")

#timer function for Pomodoro technique
def start_timer():
    try:
        timer = int(input("Enter the Pomodoro timer duration in minutes (default is 5 mins): ") or 5)
        if timer <= 0:
            return (Fore.RED + Style.RESET_ALL + "❌ Invalid duration. Please enter a positive number.")
    except ValueError:
        return (Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Invalid input. Please enter a valid number.")
    print()
    print(Fore.MAGENTA + Style.BRIGHT + f"🍅 Starting your {timer}-minute Pomodoro session. Focus mode: ON  🔒\n") ## this is the actual line for a full Pomodoro session
    # print(Fore.MAGENTA + Style.BRIGHT + f"🍅 Starting your 10 seconds Pomodoro session. Focus mode: ON  🔒\n") ## to save time during demonstration video, this line is uncommented
    # for remaining in range(10, -1, -1): ## to save time during demonstration video, this line is uncommented
    for remaining in range(timer * 60, -1, -1): ## this is the actual line for a full Pomodoro session
        mins, secs = divmod(remaining, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {time_format}", end="")
        time.sleep(1)
    print(Fore.CYAN + Style.BRIGHT + "\n🔔 Pomodoro session completed! Take a short break  🌤️")
    playsound.playsound("./sound/melodic-race-countdown.wav")
    print()

#add notes functionality
def add_notes(note = None):
    with open("./data/notes.txt", "a") as file:
        if note is None:
            note = input("Enter your note: ")
        note = note.strip()
        if not note:
            return (Fore.YELLOW + Style.RESET_ALL + "⚠️ Note cannot be empty.")
        file.write(f"{note}\n")
        return (Fore.GREEN + Style.RESET_ALL + "✅ Note added successfully.")

#view notes
def view_notes():
    with open("./data/notes.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print(Fore.YELLOW + Style.RESET_ALL + "⚠️ No notes available.")
            return
        print("Your Notes:")
        for line in lines:
            print(f"📝 {line.strip()}")

if __name__ == "__main__":
    main()