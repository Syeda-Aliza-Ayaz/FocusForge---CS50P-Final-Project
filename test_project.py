from project import add_task, mark_task_done, add_habit, add_notes
from colorama import Fore, Style, Back

def test_add_task():
    assert add_task("Test Task") == Fore.GREEN  + Style.RESET_ALL + "✅ Task added successfully."
    assert add_task("Test Task") == Fore.YELLOW + Style.RESET_ALL + "⚠️ This task already exists."
    assert add_task("") == Fore.YELLOW + Style.RESET_ALL + "⚠️ Task description cannot be empty."

def test_mark_task_done():
    assert mark_task_done(1) == Fore.GREEN + Style.RESET_ALL + "✅ Task marked as done."
    assert mark_task_done(1) == Fore.YELLOW + Style.RESET_ALL + "⚠️ This task is already marked as done."
    assert mark_task_done(999) == Fore.RED + Style.RESET_ALL + "❌ Invalid task number."
    assert mark_task_done("invalid") == Fore.RED + Style.BRIGHT + Back.WHITE + "❌ Invalid input: Please enter a valid task number."

def test_add_habit():
    assert add_habit("Test Habit") == Fore.GREEN + Style.RESET_ALL + f"✅ Habit 'Test Habit' tracked for today!"
    assert add_habit("Test Habit") == Fore.YELLOW + Style.RESET_ALL + "⚠️ You have already tracked the habit 'Test Habit' today."
    assert add_habit("") == Fore.YELLOW + Style.RESET_ALL + "⚠️ Habit description cannot be empty."

def test_add_notes():
    assert add_notes("Test Note") == Fore.GREEN + Style.RESET_ALL + "✅ Note added successfully."
    assert add_notes("") == Fore.YELLOW + Style.RESET_ALL + "⚠️ Note cannot be empty."