import speech_recognition as sr                             
import webbrowser
import pyttsx3
import music_library
import requests
from serpapi import GoogleSearch


engine = pyttsx3.init()
news_api = "4012af2677404732a24665cd20c0d4f5"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ai_script(command):
    params = {
    "engine": "google",
    "q": f"define {command}",  # Focus on retrieving definitions
    "location": "Seattle-Tacoma, WA, Washington, United States",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "num": "1",  # Limit to one result for focus
    "safe": "active",
    "api_key": "f453fbf81aa38dcfeb2974d3845fbe44044feef5001e0cfb4a2a5322287467c5"
    }

    # Fetch search results
    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract the "answer box" or definition from the response
    try:
        # Check if a dictionary definition is present
        if "knowledge_graph" in results:
            definition = results["knowledge_graph"].get("description", "No definition found.")
            print(f"Definition: {definition}")
            speak(definition)
        elif "answer_box" in results and "definition" in results["answer_box"]:
            # Handle cases where the answer box contains a definition
            definition = results["answer_box"].get("definition", "No definition found.")
            print(f"Definition: {definition}")
        else:
            print("No definition found. Please refine your query.")
    except Exception as e:
        print(f"An error occurred: {e}")

  

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
            articles = data.get('articles',[])[:10]

            for article in articles:
                print(article['title'])
                speak(article['title'])
                
    else:
        output = ai_script(c)
        print(f"Jarvis answer: {output}")
        speak(output)

def main():
    print("Initializing Jarvis........")
    speak("Initializing Jarvis")
    recognizer = sr.Recognizer()

    while True:   
        try:
            # Use the microphone as the audio source
            with sr.Microphone() as source:
                print("Please speak something...")
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=2)
            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if ("jarvis" in word.lower()):
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
            
            elif ("stop" in word.lower()):
                speak("Thank you!!See you later")
                print("Thank you!!See you later")
                break

            else:
                pass


        except Exception as e:
            print("Error; {0}".format(e))
    
if __name__ == "__main__":
    main()
    
