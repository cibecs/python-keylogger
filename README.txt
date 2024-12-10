# Keylogger Program

This is a Python-based keylogger program that records keystrokes and periodically sends the logged data to a specified webhook URL. The program uses the `keyboard` library to capture keystrokes and `requests` to send the data.

## Features
- Logs all keystrokes typed on the keyboard.
- Sends the logged keystrokes to a webhook at regular intervals (default: 10 seconds).
- Utilizes threading to handle periodic HTTP requests without interrupting the keylogging process.

---

## Requirements
- Python 3.7 or higher
- Installed dependencies: `keyboard`, `requests`

---

## Setup Instructions

### 1. Clone the Repository
Download or clone the project files to your local machine.

### 2. Create and Activate a Virtual Environment
Creating a virtual environment ensures that dependencies are managed cleanly.

#### On Windows:
1. Open a terminal in the project folder.
2. Run the following commands:
   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate

3. Install Dependencies
After activating the virtual environment, install the required packages:
    ```bash
    pip install -r requirements.txt\
    ```

### Creating an Executable
You can create an executable file for the keylogger program using `pyinstaller`.

    ```bash
    pip install pyinstaller
    ```

    ```bash
    pyinstaller --onefile keylogger.py
    ```