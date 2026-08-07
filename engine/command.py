import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 174)  # voice speed
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        eel.DisplayMessage('Listening...')
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 5, 6)

    query = ""
    try:
        eel.DisplayMessage('Recognizing...')
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        eel.DisplayMessage(f'You said: {query}')
        print("", query)

        # Wait briefly before returning to main UI
        time.sleep(0.5)

    except Exception as e:
        print("Error:", e)
        eel.DisplayMessage("Sorry, I didn’t catch that.")
        eel.ShowHood()
        return ""

    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
       query = takecommand()
       print(query)
    else:
        query = message


    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
    else:
        from engine.features import geminai
        geminai(query)

      # Switch back to hood screen
    eel.ShowHood()