# Jarvis_Virtual_assistant

---

# 🤖 JARVIS: Advanced Virtual Assistant

**JARVIS** (Just A Rather Very Intelligent System) is a dual-interface voice assistant. It features a desktop-based automation script and a stunning, futuristic web interface inspired by Iron Man's Arc Reactor.

## ✨ Features

* **🎙️ Dual Mode Interaction**: Use the CLI via `main.py` for direct system control or the Web UI via `app.py`.
* **🧠 Personal Memory**: Remembers your name and favorite programming language using `memory.json`.
* **🎵 Smart Music Library**: Integrated playback for your favorite tracks (Radha, Perfect, Snowman, etc.) with partial match search.
* **🌐 Web Automation**: Quick commands to open Google, YouTube, and LinkedIn.
* **📰 Live News**: Fetches the top 5 global headlines on demand.
* **🤖 Gemini AI Integration**: For queries not handled by local logic, JARVIS consults Google's Gemini Flash model for intelligent responses.

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt

```

### 2. Configuration

Open `jarvis_core.py` and ensure your API keys are set (or use environment variables):

* **NewsAPI**: Used for fetching headlines.
* **Gemini API**: Powering the advanced AI reasoning.

### 3. Running JARVIS

You can run JARVIS in two ways:

**Option A: The Web Interface (Recommended)**

```bash
python app.py

```

*Navigate to `http://127.0.0.1:5000` to see the animated Arc Reactor boot sequence.*

**Option B: The Desktop Assistant**

```bash
python main.py

```

*Say **"Jarvis"** to wake him up and start giving commands.*

---

## 🛠️ Project Structure

| File | Description |
| --- | --- |
| `app.py` | Flask server hosting the web interface. |
| `main.py` | Local voice recognition loop (Wake word: "Jarvis"). |
| `jarvis_core.py` | The "Brain" containing command logic and AI processing. |
| `musicLibrary.py` | Dictionary of songs and their YouTube links. |
| `index.html` | Futuristic UI with CSS animations and Speech-to-Text. |
| `memory.json` | Persistent storage for user preferences. |

---

## ⌨️ Example Commands

* **Identify Yourself**: *"My name is Upasana"* → *"What is my name?"*
* **Music**: *"Play Snowman"* or *"Play Perfect"*
* **Web**: *"Open YouTube"* or *"Open LinkedIn"*
* **Knowledge**: *"How does quantum computing work?"* (Handled by Gemini AI)
* **Updates**: *"Give me the news"*

---

## 🎨 UI Preview

The web interface features a custom **Boot Sequence** that checks system modules before initializing the voice interface. The Arc Reactor pulses rhythmically and speeds up when JARVIS is actively "listening" to your commands.

---

## 🤝 Contributing

Feel free to fork this project, add new songs to `musicLibrary.py`, or expand the `processCommand` logic in `jarvis_core.py` to support more automation!

**Developed by Upasana**

---


