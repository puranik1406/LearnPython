import time
from plyer import notification
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while(True):
    notification.notify(title="Drink Water",message="It's been 2 hours since you drank water!!",app_icon=r"C:\Users\ishit\PythonLearn\water.ico",timeout=5)
    speaker.Speak("Drink Water!!")
    time.sleep(7200)