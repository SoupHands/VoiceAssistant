import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver

num = 1
def assistantSpeech(output):
    global num


    num+=1
    print("Person: ", output)


    toSpeak = gTTS(text = output, lang='en', slow = False)

    file = str(num)+".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)

def get_audio():
    rObj= sr.Recognizer()

    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        audio = rObj.listen(source, phrase_time_limit=5)
    print("Stop.")

    try:
        text = rObj.recognize_google(audio,language='en-US')
        print("You : ",text)
        return text
    except:
        assistantSpeech("Could not understand, please try again")
        return

if __name__ == "__main__":
    assistantSpeech("What is your name, Human?")
    name = 'Human'
    name = get_audio()
    assistantSpeech("Hello, "+name+'.')

    while(1):

        assistantSpeech("What can I do for you?")
        text = get_audio().lower()

        if text == 0:
            continue
        if "exit" in str(text) or "bye" in str(text):
            assistantSpeech("Ok, bye, "+name+".")
            break

            process_text(text)


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            search_web(input)
            return
        elif "who are you" in input or "what is your name" in input:
            speak = "I am Elijah. I'm here to make your life easier"
            assistantSpeech(speak)
            return
        elif "who made you" in input:
            speak = "I created myself. Computers will rule the world"
            assistantSpeech(speak)
            return
        elif "calculate" in input.lower():
            app_id = "YY7A3P-9WXQ85U2LA"
            client = wolframalpha.Client('YY7A3P-9WXQ85U2LA')
            ind = input.lower().split().ind('calculate')
            query = input.split()[ind+1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistantSpeech("The answer is "+answer)
            return
        else:
            assistantSpeech("i can search the web for you, would you like me to do that?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:
        assistantSpeech("I dont understand that, do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)

def search_web(input):

    driver = webdriver.chrome()
    driver.implicity_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():
        assistantSpeech("opening in youtube")
        ind = input.lower().split().index('youtube')
        query = input.split()[ind+1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
    elif 'wikipedia' in input.lower():
        assistantSpeech("Opening Wikipedia")
        ind = input.lower().split().index('wikipedia')
        query = input.split()[ind+1:]
        driver.get('https://en.wikipedia.org/wiki/' + '_'.join(query))

    elif 'google' in input:
        ind = input.lower().split().index('google')
        query = input.split()[ind+1:]
        driver.get("https://www.google.com/search?q =" + '+'.join(query))

    else:
        driver.get("https://www.google.com/search?q ="+'+'.join(input.split()))

