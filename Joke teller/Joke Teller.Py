"""
Random Joke Generator and Speaker
Author: Dibyjyoti Mishra
Description: A simple Python script that fetches a random joke using the 
pyjokes library and reads it aloud using the pyttsx3 text-to-speech engine.
"""

import pyjokes
import pyttsx3

try:
    # Fetch a single joke
    joke = pyjokes.get_joke()
    print(joke)
    
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    engine.say(joke)
    engine.runAndWait()
    
except Exception as e:
    print(f"Error: {e}")
    print("Make sure pyjokes and pyttsx3 are installed: pip install pyjokes pyttsx3")
