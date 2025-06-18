# 🧠 Smart Scheduler AI Agent

This is a voice-enabled AI assistant that helps users schedule meetings via natural conversation. It understands spoken inputs, identifies time and duration preferences, checks Google Calendar availability, and schedules meetings seamlessly.

## 🚀 Features

- 🎤 Voice input and output (speech-to-text and text-to-speech)
- 📅 Google Calendar integration
- 🤖 Smart conversation handling and intent recognition
- ⏰ Natural language time and date parsing
- 🔁 Multi-turn dialogue with contextual memory

---

## 📦 Tech Stack

- **Python 3.13+**
- **Google Calendar API**
- **Google Gemini API**
- **ElevenLabs TTS (v2.3.0 SDK)**
- `SpeechRecognition`, `PyAudio`, `datetime`, `dateparser`, `google-auth`, `google-api-python-client`, etc.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ayushranjan11/Ayushranjan11-smart-scheduler-ai-agent.git
cd Ayushranjan11-smart-scheduler-ai-agent
```

### 2. Create Virtual Environment and Activate

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root directory with the following:

```
ELEVENLABS_API_KEY=your_elevenlabs_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

> Get ElevenLabs key from https://www.elevenlabs.io  
> Get Gemini key from https://makersuite.google.com/app/apikey

### 5. Set Up Google Calendar

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Google Calendar API**
- Create **OAuth 2.0 credentials** (Desktop App)
- Download the `credentials.json` file and place it in the project root

The first time you run the app, it will prompt for Google auth and create a `token.json`.

---

## ▶️ Run the App

```bash
python main.py
```

The app will:
- Greet you
- Ask what you want to do
- Take meeting duration and time
- Suggest or book the meeting in Google Calendar

---

## 🧠 How It Works

1. **Voice Layer:** Uses SpeechRecognition to capture user voice and convert it to text.
2. **LLM Layer:** Gemini Pro interprets the user's intent, maintains context (like meeting duration), and handles conversation flow.
3. **TTS Layer:** ElevenLabs speaks responses naturally using low-latency text-to-speech.
4. **Calendar Tool:** Authenticates and interacts with Google Calendar to find or create events.
5. **Scheduling Logic:** Checks for conflicts, suggests alternatives, confirms, and books the meeting.

---

## 🧩 Design Decisions

- **Modular structure**: Each component (voice, LLM, calendar) is separated for clarity and easy updates.
- **Free tools only**: Avoided paid services like Vapi/Make/Bland.ai.
- **Custom parsing logic**: Uses `dateparser` to convert user-friendly time inputs into proper datetime.
- **Basic conflict resolution**: If a slot is booked, agent asks for alternative suggestion.
- **Conversational state**: Context like duration is preserved across dialogue turns.

---

## 📹 Demo Video

*A 2–3 minute screen recording showing:*
- Voice conversation
- Calendar event being created live
- Voice confirmation and fallback handling

✅ Coming soon...

---

## 📧 Contact

By [Ayush Ranjan](https://github.com/Ayushranjan11)
