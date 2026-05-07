"""
Random Joke Generator and Speaker
Author: Dibyjyoti Mishra
Description: A simple Python script that fetches a random joke using the 
pyjokes library and reads it aloud using the pyttsx3 text-to-speech engine.
"""

import pyjokes

import pyttsx3

all_jokes = pyjokes.get_joke()
print(all_jokes)

engine = pyttsx3.init()
engine.say(all_jokes)    
engine.runAndWait()