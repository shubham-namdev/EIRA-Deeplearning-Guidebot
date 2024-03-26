'''
Contains Functions Used during Training and execution

'''
import pyttsx3
import nltk
from nltk.stem.porter import PorterStemmer
import speech_recognition as sr
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import random
import json
from model import NeuralCode
import pyglet

"""
Un-comment this line while runnning for the first time.
"""
# nltk.download('punkt')


'''Functions'''

# tokenize sentence
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


# Stem word to root
def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())


# Bag of words (vocabulary builder for bot)
def bag_of_words(tokenized_sentence, all_words):
    """
    sentence = "Hello there"
    words = ['hello', 'bye', 'there']
    bag   = [   1   ,   0  ,    1   ]
    """
    tokenized_sentence = [stem(word) for word in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[idx] = 1.0

    return bag
    '''
    sentence = ["hey", "how", "are", "you"]
    words =  ["hey", "hello", "how", "we", "are", "they", "you"]   
    bag = bag_of_words(sentence,words)    
    print(bag)
    '''


# Speech to text
def recognizer():
   
    key = 'n'
    sender = "You"
    
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
    except OSError:
        txt = "TECHNICAL ERR. (MICERR) :{"
        key = 'm'
        sender = "EIRA"
        return txt, key, sender      
    
    
    try:
        txt = r.recognize_google(audio)
        
    except sr.UnknownValueError:
        key = 'a'
        sender = "EIRA"
        txt = "Sorry I didn't understand. Can you please repeat?"
        return txt, key, sender
    
    except sr.RequestError :
        txt = "SERVERS ARE DOWN :/ "
        key = 'e'
        sender = "EIRA"
        return txt, key, sender
    
    return txt, key, sender


# Play mp3 files
def play(mp3_file):
    
    music = pyglet.resource.media(mp3_file)
    music.play()
    pyglet.app.run()
    pyglet.app.exit()
    return
 

# Text to speech (offline)
def talk(text):
    # initialisation
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 150)
    # running
    engine.say(text)
    engine.runAndWait()

