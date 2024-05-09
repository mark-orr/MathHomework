import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(0,1):
    engine.setProperty('voice', voices[i].id)
    engine.say("Would You Like To Play A Game?")
    print(i,'\n')
    engine.runAndWait()

