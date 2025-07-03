import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import pyjokes #pip install pyjokes
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("What's your mood to do today sir!")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            # If the user asks for something on Wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try :
                results = wikipedia.summary(query, sentences=3)
                # Print the results to the console
                print("According to Wikipedia:")
                print(results)
                # Speak the results
                speak("According to Wikipedia")
                speak(results)
                # Check if the spoken results match the printed results
                assert results in str(results), "The spoken results do not match the printed results."

            except Exception as e:
                print("Sorry, I couldn't find that on Wikipedia.")
                speak("Sorry, I couldn't find that on Wikipedia.")

        elif "let's play a game" in query:
            speak("Ok sir, guess a number, and say done if you're ready")
            num1 = takeCommand()
            speak("ok sir, now double the number in your mind")
            num2 = 2*num1
            speak("Now add my 12 to the answer you got")
            done = speak("say done")
            reply = takeCommand()
            speak("Half the number")
            reply2 = takeCommand()
            speak("subtract the initial number")
            reply3 = takeCommand()
            speak("the answer is 6")

        elif 'open in four wheeler' in query:
            webbrowser.open("informvilla.blogspot.com")
            speak("Sure sir, opening Infovilla")
            print("Opening Infovilla...")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Sure sir, opening Youtube")
            print("Opening Youtube...")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Sure sir, opening Google")
            print("Opening Google...")

        elif 'are you there' in query:
            speak("yes, I am there! sir")

        elif 'are you sleeping' in query:
            speak("No sir, I never sleep")

        elif 'your name' in query:
            speak("My name is Jarvis AI Assistant")

        elif 'alarm' in query:
            speak("What's the worksir!")
            WORK = takeCommand()
            speak("Alright sir, Enter the time please")
            time = input("Enter the time sir:\n")
            speak("Alarm setted for "+time)

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M")

                if now == time:
                    speak("Time to "+WORK)

                elif now > time:
                    break
                                           
        elif 'thank you' in query:
            speak("You're most welcome sir")

        elif "sorry" in query:
            speak("No, Sir mistakes a man, I never mind it sir!")  

        elif "talk to you" in query:
            speak("yes please, it will be my pleasure!")

        elif "are you connected" in query:
            speak("yes I am connected to the internet all time")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'hi jarvis' in query:
            hi = "Hello sir, please tell me how may I help you!"
            print(hi)
            speak(hi)

        elif 'hello jarvis' in query:
            hello = "Hello sir, please tell me how may I help you!"
            print(hello)
            speak(hello)

        elif 'who made you' in query:
            create = "Ayush Kumar Singh created me, with the use of python along with the hardwork of 24hrs"
            speak(create)

        elif 'who created you' in query:
            create = "Ayush Kumar Singh created me, with the use of python along with the hardwork of 24hrs"
            speak(create)

        elif 'how are you' in query:
            speak("I am Fine sir, what about you")

        elif 'I am fine' in query:
            speak("Alright sir, what can I do for you!")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'exit' in query:
            speak("Thankyou sir, Nice to talk to you")
            exit()