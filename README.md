# Jarvis_Virtual_assistant

🤖 JARVIS – AI Voice Assistant with Web UI (Iron Man Style)

JARVIS is a smart AI-powered voice assistant inspired by Iron Man’s JARVIS.
It combines Python, Flask, Gemini AI, Speech Recognition, and a futuristic web UI with an animated Arc Reactor interface.

This project supports voice commands, AI conversations, memory storage, music playback, news fetching, and works in both Web UI and Desktop Voice mode.

🚀 Features

🎙️ Voice Command Recognition (Wake word: Jarvis)

🧠 AI Responses using Google Gemini API

🌐 Web-based UI with Iron Man–style Arc Reactor animation

🔊 Text-to-Speech Output (Cleaned speech – no symbols spoken)

🗂️ Persistent Memory System

Remembers user name

Remembers favorite programming language

🎵 Music Playback via YouTube

📰 Live News Headlines (NewsAPI)

🔗 Quick Commands

Open Google

Open YouTube

Open LinkedIn

👨‍💻 Dual Mode

Web-based Assistant

Desktop Voice Assistant (Terminal-based)

🛠️ Tech Stack

Frontend

HTML5

CSS3 (Animations & UI Effects)

JavaScript (Speech Recognition & Speech Synthesis)

Backend

Python

Flask

Google Gemini AI

SpeechRecognition

Pyttsx3

NewsAPI

📁 Project Structure
JARVIS/
│── app.py                # Flask web server
│── jarvis_core.py        # Core AI logic & command processing
│── main.py               # Desktop voice assistant
│── musicLibrary.py       # Custom music database
│── memory.json           # Persistent memory storage
│── requirements.txt      # Project dependencies
│
├── templates/
│   └── index.html        # Web UI (Arc Reactor + Voice UI)

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 API Configuration

Update your API keys inside jarvis_core.py:

newsapi = "YOUR_NEWS_API_KEY"
api_key = "YOUR_GEMINI_API_KEY"


⚠️ Do NOT expose API keys in public repositories
Use environment variables for production.

▶️ Run the Project
🌐 Web-Based JARVIS
python app.py


Open browser:

http://127.0.0.1:5000

🎧 Desktop Voice Assistant
python main.py


Say “Jarvis” to activate 🎙️

🗣️ Example Voice Commands
Open Google
Play perfect
What's the news
My name is Upasana
What is my name
My favorite language is Python
What is my favorite language

🧠 Memory System

JARVIS stores user information in memory.json:

{
  "name": "Upasana",
  "favorite_language": "Python"
}


Memory persists even after restarting the application.

📸 UI Preview

✨ Arc Reactor Animation
✨ Boot-up Sequence
✨ Voice Listening & Processing Effects

(Inspired by Iron Man’s JARVIS)

🧩 Future Enhancements

Emotion-based reactions (Happy / Alert / Neutral)

Male/Female voice selection

Authentication system

Cloud deployment

Mobile-friendly UI

Command history & analytics

👩‍💻 Author

Upasana Prajapati
🎓 BCA | Data Science | AI & Python Developer
🔗 LinkedIn

⭐ Support

If you like this project, please ⭐ star the repository
and feel free to fork & contribute!
