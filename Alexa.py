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
    elif 'Are you single' in command:
        cmd = talk('I am in a relationship with WiFi')
        print(cmd)
    elif 'In which standard you are' in command:
        cmd = talk('I am in a 11th standard')
        print(cmd)
    elif 'How are you' in command:
        cmd = talk('I am fine, thanks for asking')
        print(cmd) 
    elif 'Can you dance' in command:
        cmd = talk('I am learning hip hop now, thanks for asking')
        print(cmd) 
    elif 'Are you happy' in command:
        cmd=talk('Yes,I am ,as I can help you!')
        print(cmd)    
    elif 'Where were you last night?' in command:
        cmd=talk('Ask you mom.')
        print(cmd)  
    elif 'Can you give me a random fact?' in command:
        cmd=talk("There's a Valentine's Day for Single People in South Korea , perfect place for you!")
        print(cmd)   
    elif 'What is Engineering ?' in command:
        cmd=talk('the work of designing and creating large structures')
        print(cmd)       
    elif 'Where do you live?' in command:
        cmd=talk('I live in globalized world')
        print(cmd)
    elif 'Where is west located?' in command:
        cmd=talk('West is west to east and south to north and north to south')
        print(cmd)
    elif 'What is two into two?' in command:
        cmd=talk('Four')
        print(cmd) 
    elif 'what is the square of two?' in command:
        cmd=talk('four')
        print(cmd) 
    elif 'Are you a Robot?' in command:
        cmd=talk('I am a human robot ')
        print(cmd)  
    elif 'Tell me a joke ?' in command:
        cmd=talk('Relationships are a lot like algebra. Have you ever looked at your X and wondered Y?')
        print(cmd)
    elif 'from which city I am from' in command:
        cmd=talk('I ask google map ')
        print(cmd)    
    elif 'How is your mood?' in command:
        cmd=talk('Depressed as yours!')
        print(cmd)
   elif 'Tell me fun fact about the world' in command:
        cmd=talk('Sudan has the most pyramids in the world (not Egypt).')
        print(cmd)
   elif 'Which is the coolest club in WCE?' in command:
        cmd=talk('Google developers Students Club WCE!')
        print(cmd)
    else:
       default = talk('I am sorry, I did not understand ')
       print(default)
        
call_Anuja()
