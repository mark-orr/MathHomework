import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(3,10):
    engine.setProperty('voice', voices[i].id)
    engine.say("Would You Like To Play A Game?")
    print(i,'\n')
    engine.runAndWait()

