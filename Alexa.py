import speech_recognition as event
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes

listener = event.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text

def listening_Anuja():
    try:
        talk('Hey I am Anuja, What can I do for you')
        with event.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            
    except:
        pass
    return command

def call_Anuja():
    command = listening_Anuja()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing ' + song)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = talk(pyjokes.get_joke())
        print(joke)
    elif 'are you single' in command:
        cmd = talk('I am in a relationship with WiFi')
        print(cmd)
    elif 'Hello,Who are you' in command:
        cmd = talk('I am Arshad')
        print(cmd)
    elif 'how are you' in command:
        cmd = talk('I am fine, thanks for asking')
        print(cmd)
    elif 'What is your name?' in command:
        cmd=talk('My name is alexa')
        print(cmd)
    elif 'Do u know siri?' in command:
        cmd=talk('Yeah! She is my good friend')
        print(cmd)    
    else:
       default = talk('I am sorry, I did not understand')
       print(default)
        
call_Anuja()
