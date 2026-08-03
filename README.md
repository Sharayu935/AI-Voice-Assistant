# AI Voice Assistant

## An Intelligent Desktop Voice Assistant Built with Python and Eel

AI Voice Assistant is a desktop automation application that allows users to interact with their computer using voice commands. It listens to user input, converts speech into text, processes commands, and performs various tasks such as opening applications, searching the web, and responding through text-to-speech.

The project combines Python for backend processing with HTML, CSS, JavaScript, Bootstrap, and Eel to provide a modern desktop interface.

# Overview

The AI Voice Assistant is designed to simplify everyday computer operations through voice interaction. It provides an intuitive interface and supports automation of common tasks while demonstrating the integration of speech recognition, desktop automation, database management, and web technologies.

# Features

## Voice Recognition

* Recognizes voice commands
* Converts speech into text
* Supports continuous voice interaction

## Text-to-Speech

* Converts text into speech
* Provides voice responses
* Improves user interaction

## Web Automation

* Open websites
* Search information on Google
* Open YouTube and other web applications

## Desktop Automation

* Open Calculator
* Open Notepad
* Launch desktop applications

## Database Integration

* SQLite database support
* System command mapping
* Web command mapping

## User Interface

* Responsive interface
* Animated voice wave
* Simple and modern design

# Project Architecture

                     User
                       │
               Voice/Text Command
                       │
              Speech Recognition
                       │
                Command Processing
                       │
        ┌──────────────┴──────────────┐
        │                             │
   System Commands             Web Commands
        │                             │
   Open Applications         Search/Open Websites
        │                             │
        └──────────────┬──────────────┘
                       │
                    Response


# Technology Stack

## Backend

* Python
* Eel
* SpeechRecognition
* pyttsx3
* SQLite3
* pywhatkit
* pyautogui

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* jQuery

This project uses several open-source Python libraries and web technologies, including Eel, SpeechRecognition, pyttsx3, Bootstrap, and SQLite.
