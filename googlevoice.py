from gtts import gTTS
import os
text = input("Enter your text: ")
language = 'en'
audio_object = gTTS(text=text, lang=language, slow=False)
audio_object.save("output.mp3")
os.system("start output.mp3") # Plays the audio on Windows

#print((gtts.lang.tts_langs()))