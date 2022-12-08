import pyttsx3
tts = pyttsx3.init()
while True:
    tts.say('Yura, do your homework!')
    tts.runAndWait()
    tts.say('Yura, delay uroki! Bistro! Ne smotri vidosiki!')
    tts.runAndWait()
