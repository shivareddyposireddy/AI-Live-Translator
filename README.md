# 🌍 AI Live Translator

AI-powered real-time multilingual communication system using speech recognition, translation, and voice synthesis.

---

# 🚀 Overview

AI Live Translator enables users speaking different languages to communicate seamlessly in real time.

The system:
- converts speech into text,
- translates the text into another language,
- and generates translated voice output.

---

# ✨ Features

✅ Real-time microphone recording  
✅ AI speech recognition using Whisper  
✅ Multilingual translation  
✅ AI-generated translated voice  
✅ Streamlit frontend  
✅ FastAPI backend  
✅ Real-time communication workflow  

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI

## AI / NLP
- Faster-Whisper
- Deep Translator
- gTTS

---

# 🔄 System Workflow

User Voice Input
↓
Speech Recognition (Whisper)
↓
Language Detection
↓
Translation Engine
↓
Text-to-Speech
↓
Translated Voice Output

---

# 🌐 Supported Languages

- English
- Hindi
- Telugu
- Tamil
- Kannada

---

# 📁 Project Structure

```text
ai-live-translator/
│
├── backend/
├── frontend/
├── docs/
├── tests/
└── README.md
```

---

# ⚙️ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger API docs:

```text
http://127.0.0.1:8000/docs
```

---

# ⚙️ Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
python -m streamlit run app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# 📸 Screenshots

(Add screenshots here)

---

# 🎥 Demo Video

(Add demo video link here)

---

# 🔮 Future Enhancements

- Real-time streaming translation
- Speaker identification
- Noise suppression
- Offline mode
- WebSocket communication
- Emotion-aware translation

---

# 👨‍💻 Author

Shiva Reddy

Final Year B.Tech CSE Student  
Aspiring AI & Data Analyst Engineer