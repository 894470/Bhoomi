# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 04:16:06 2020

@author: DELL
"""

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import wolframalpha
#for weather 
try:
    app = wolframalpha.Client("R2G79G-JTKE9Y89KG")
except Exception:
    print("connection failed")

    

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#to convert voice to text
def takecommand():
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3,phrase_time_limit = 5)
        
        
        try:
            print('recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:  {query} ")
            
        except Exception as e:
            speak('say that again please')
            return "none"
        return query
            
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('hi, myself Bhoomi, how can i help you')
          
#def sendEmail(to,content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('jjdaskosi@gmial.com', 'kosijjdas@1234')
    #server.sendmail('jjdaskosi@gmail.com',to,content)
    #server.close()    
    
if __name__ == '__main__':
    
    wish()
    
    while True:
        if 1:
        
            query = takecommand().lower()
        
            #logic buliding for tasks
        
            if "open google" in query:
                speak("sir what should i search in google")
                tw = takecommand().lower()
                tc = webbrowser.open(f"{tw}")
                
            elif "close" or "exit" or "no thanks" in query:
                speak('thanks for your interaction, may the force be with you')
                sys.exit()
            
            
            elif "play music" in query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
            
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is{ip}")
                
            elif "wikipedia" in query:
                speak('searching wikipedia....')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak('according to wikipedia')
                speak(results)
                print(results)
            
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")
                
            elif "play song on youtube" in query:
                speak("which song should play")
                song = takecommand().lower()
                speak("now playng")
                kit.playonyt(song)
            
                
            #elif "email to" in query:
                #try:
                    #speak("what should i say")
                    #content = takecommand().lower()
                    #to = "saianish07@gmail.com "
                    #sendEmail(to,content)
                    #speak("email has been sent you anish")
                #except Exception as e:
                    #print(e)
                    #speak('sorry sir im not able to send this email')
            
            elif "weather" or "temparature" or "humidity" in query:
                try:
                    res = app.query(query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except:
                    speak('network connection failed')
            
            elif "send message" in query:
                for i in range(10):
                    kit.sendwhatmsg("+91 79757 99132", "'ootak baare sade fuck you'+i",12,50)
             
            
            speak('do you have any other thing to say')    
                
                
    
    