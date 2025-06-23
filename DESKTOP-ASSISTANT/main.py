import speech_recognition as sr                             
import webbrowser
import pyttsx3
import music_library
import requests
import openai

engine = pyttsx3.init()

news_api = "4012af2677404732a24665cd20c0d4f5"

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
openai.api_key="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"

def ai_script(command):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": command}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I encountered an error while processing your request."

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/GiggaCat")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/vansh-arora-5b45b3292?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging_conversation_detail%3B%2BLje80a8QxCVLDPfl626cA%3D%3D")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])

            for article in articles:
                print(article['title'])
                speak(article['title'])
                break
    else:
        output = ai_script(c)
        print(f"Jarvis answer: {output}")
        speak(output)


if __name__ == "__main__":
    print("Initializing Jarvis........")
    speak("Initializing Jarvis")
    while True:
        recognizer = sr.Recognizer()
        
        try:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                print("Please speak something...")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print("You said:", word)
            if (word.lower() == "hi jarvis" or word.lower() == "hello"):
                speak("Greeting master")
                print(f"Jarvis said: Greeting master")
                with sr.Microphone() as source:
                    print("Jarvis Active.......")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)  
                    print("You said:", command)
                    speak("sure,master")
                    print("Sure,master")
                    process_command(command)
            
            elif (word.lower() == "stop"):
                speak("Thank you!!See you later")
                print("Thank you!!See you later")
                break


        except Exception as e:
            print("Error; {0}".format(e))
    