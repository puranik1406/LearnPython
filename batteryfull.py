import psutil
from plyer import notification
import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

alerted = False  # flag to avoid spamming notifications

while True:
    battery = psutil.sensors_battery()
    
    if battery.percent == 100 and battery.power_plugged:
        notification.notify(
            title="Battery Full",
            message="Your laptop battery is full, turn off the switch",
            app_icon=r"C:\Users\ishit\GitRepos\PythonLearn\Battery icon.ico",
            timeout=7
        )
        speaker.Speak("Battery Full! Turn off the switch!")
    
    time.sleep(60)  # alert every 60 seconds until power is unplugged
