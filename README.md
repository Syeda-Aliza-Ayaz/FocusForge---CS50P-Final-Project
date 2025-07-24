# 🎯 FocusForge

**FocusForge** is a command-line productivity app built with Python to help users stay organized and focused. It provides tools to manage tasks, track habits, take notes, and boost productivity using the Pomodoro Technique. Designed with simplicity and modularity, it demonstrates Python fundamentals like data handling, file I/O, functions, user input validation, modular structure, and unit testing.

---

## 📽️ Demo Video

👉 [Click here to watch the demo](https://youtu.be/cXA3GDqisKM)

---

## 📦 Features

- ✅ **To-Do List**: Add, edit, mark complete, and delete tasks, stored in JSON format.
- 🔁 **Habit Tracker**: Track daily habits with date history, saved in JSON format.
- 🗒️ **Notes Section**: Write and view quick notes, stored in a text file.
- ⏱️ **Pomodoro Timer**: Customizable countdown timer (default 5 minutes) with an audio alert upon completion.
- 🎨 **Vibrant CLI UI**: Uses `pyfiglet` for an ASCII banner and `colorama` for colored output with expressive emojis.
- 🔊 **Sound Notification**: Plays a `.wav` audio alert (`melodic-race-countdown.wav`) at the end of each Pomodoro session.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)

## Install Testing Dependencies:

The requirements.txt file includes libraries such as pyfiglet, colorama, playsound, and pytest.

4. **Run the App**:

```bash
python project.py
```

Note: Ensure the /data and /sound directories exist. The /data folder stores tasks.json (tasks), habits.json (habits), and notes.txt (notes). The /sound folder contains melodic-race-countdown.wav for Pomodoro alerts.

## 🖥️ Usage Examples
After running python project.py, FocusForge displays an ASCII banner and an interactive menu. Below are example interactions:


### Add a Task:

```text
Select an option: 1
Enter your choice: 1
Enter the task description: Finish CS50P project
✅ Task added successfully.
```


### Start Pomodoro Timer:

```text
Select an option: 3
Enter the Pomodoro timer duration in minutes (default is 5 mins): [Enter]
🍅 Starting your 5-minute Pomodoro session. Focus mode: ON 🔒
⏳ Time left: 05:00 [counts down]
🔔 Pomodoro session completed! Take a short break 🌤️
[Plays melodic-race-countdown.wav]
```

### Track a Habit:

```text
Select an option: 2
Enter your choice: 1
Enter the habit you want to track: Drink 2L water
✅ Habit 'Drink 2L water' tracked for today!
```

### Write a Note:

```text
Select an option: 4
Enter your choice: 1
Enter your note: Review README for submission
✅ Note added successfully.
```

- Use the menu to navigate features. Type 5 in the main menu to exit.

## 🧪 Running Tests
Unit tests for task management, habit tracking, and notes are included in `test_project.py` using pytest.

## Install Testing Dependencies:
    ```bash
    pip install pytest
    ```
    
### Run Tests:
    ```bash
    pytest test_project.py -v
    ```
    
Expected Output: Tests verify core functionality (e.g., adding tasks, tracking habits). All tests should pass if the app is working correctly.
Note: Ensure the /data directory exists, as some tests may interact with stored files. Moreover, if you want to run tests more than once, make sure to either change the arguments of the first tests of every function, or remove the tasks and habits added by running `pytest`, else the tests might fail.

## 📂 File Structure
    ```text
    FocusForge/  
    │  
    ├── project.py                    # Main app logic  
    ├── test_project.py              # Unit tests with pytest  
    ├── requirements.txt             # Dependencies list  
    │  
    ├── data/                        # Stores JSON and text files  
    │   ├── tasks.json              # Task data  
    │   ├── habits.json             # Habit history  
    │   └── notes.txt               # Notes  
    │  
    ├── sound/                       # Audio alert  
    │   └── melodic-race-countdown.wav  # Pomodoro completion sound  
    ```
    
## 📄 License  
- This project is licensed under the MIT License. See the LICENSE file for details.

## 👩‍💻 Author
**Name:** Syeda Aliza Ayaz
**GitHub:** [Syeda-Aliza-Ayaz](https://github.com/Syeda-Aliza-Ayaz/FocusForge---CS50P-Final-Project.git)
**edX Username:** Syeda-Aliza-Ayaz
**Location:** Karachi, Pakistan

### 🙌🏻 Proudly submitted as the final project for CS50’s Introduction to Programming with Python.
