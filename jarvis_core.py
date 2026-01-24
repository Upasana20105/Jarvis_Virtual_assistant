import webbrowser
import requests
import musicLibrary
from google import genai
import json
import os

# jarvis_core.py
memory = {}
MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


newsapi = "d95a530c53f44691b9172b1b50fd6f10"

def aiProcess(command):
    client = genai.Client(
        api_key="WRITE_YOUR_OWN_API_KEY",
        http_options={'api_version': 'v1'}
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=command
    )
    return response.text


def processCommand(command):
    print("Command:", command)
    c = command.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com/in/upasana-prajapati")
        return "Opening LinkedIn"

    elif c.startswith("play"):
        song = c.replace("play", "").strip()

        # Try exact match first
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            return f"Playing {song}"

        # Try partial match (BEST FEATURE)
        for key in musicLibrary.music:
            if key in song:
                webbrowser.open(musicLibrary.music[key])
                return f"Playing {key}"

        return "Song not found in your music library"


    elif "news" in c:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        )
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            headlines = [a["title"] for a in articles[:5]]
            return "Here are the headlines. " + ". ".join(headlines)
        else:
            return "Unable to fetch news"

    
    elif "my name is" in c:
        
        name = c.replace("my name is", "").strip().title()
        memory["name"] = name
        save_memory(memory)
        return f"Nice to meet you, {name}. I will remember your name."
    
    elif "what is my name" in c or "do you know my name" in c:
        name = memory.get("name")
        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet. You can tell me by saying, my name is..."
        
    elif "my favorite language is" in c:
        lang = c.replace("my favorite language is", "").strip().title()
        memory["favorite_language"] = lang
        save_memory(memory)
        return f"Got it. I will remember that your favorite language is {lang}."
        
    elif "what is my favorite language" in c:
        lang = memory.get("favorite_language")
        if lang:
            return f"Your favorite programming language is {lang}."
        else:
            return "You haven't told me your favorite language yet."

        


        
    else:
        memory = load_memory()
        return aiProcess(command)

