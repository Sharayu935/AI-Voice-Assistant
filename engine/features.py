import re
from shlex import quote
import sqlite3
import subprocess
import time
import webbrowser

import pyautogui
from engine.config import ASSISTANT_NAME, LLM_KEY
from engine.command import speak
import os
import pywhatkit as kit

from engine.helper import remove_words, markdown_to_text

con = sqlite3.connect("AI.db")
cursor = con.cursor()

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path From sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("opening "+query)
                    webbrowser.open(results[0][0])

                else: 
                    speak("opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")

        except:
            speak("Something went wrong")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    # define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # if a match is found, return the extracted song name otherwise return none
    return match.group(1) if match else None

# find contacts

def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

# whatsapp message sending    
 
def whatsApp(mobile_no, message, flag, name):
    import pyautogui, time, subprocess
    from shlex import quote
    from engine.command import speak

    if flag == 'message':
        jarvis_message = "Message sent successfully to " + name
    elif flag == 'call':
        message = ''
        jarvis_message = "Calling " + name
    elif flag == 'video call':
        message = ''
        jarvis_message = "Starting video call with " + name


    encoded_message = quote(message)

    # Construct WhatsApp Desktop link
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp Desktop chat
    subprocess.run(full_command, shell=True)
    time.sleep(5)  # wait for the app to open and load chat window

    # Bring WhatsApp window to focus (use twice for reliability)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

    # Press Enter to send message
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')  # double press for safety

    if flag == 'video call':
       time.sleep(2)
    # Adjust coordinates based on your screen resolution and WhatsApp layout
    # Open video call button (usually top-right corner)
       pyautogui.moveTo(1700, 90)  # Example coordinates
       pyautogui.click()


    speak(jarvis_message)

import google.generativeai as genai
def geminai(query):
    try:
        query = query.replace(ASSISTANT_NAME, "")
        query = query.replace("search", "")
        # set your api key
        genai.configure(api_key=LLM_KEY)

        # select a model
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Generate a response
        response = model.generate_content(query)
        filter_text = markdown_to_text(response.text)
        print(filter_text)
        speak(filter_text)
    except Exception as e:
        print("error:", e)