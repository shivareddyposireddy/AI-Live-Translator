# Backend - AI Live Translator

FastAPI backend for multilingual speech translation system.

---

# 🚀 Features

- Speech-to-text using Faster-Whisper
- Language translation
- Text-to-speech generation
- REST API endpoints

---

# 🛠 Technologies

- FastAPI
- Faster-Whisper
- Deep Translator
- gTTS

---

# 📁 Backend Structure

```text
backend/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── main.py
```

---

# ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

# 🌐 API Endpoints

## Speech-to-Text

```text
POST /speech/to-text
```

---

## Translation

```text
POST /translate
```

---

## Text-to-Speech

```text
POST /tts
```

---

# 📖 Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🔄 Backend Workflow

Audio Input
↓
Whisper Speech Recognition
↓
Translation Engine
↓
Voice Generation
↓
API Response

---

# 👨‍💻 Author

Shiva Reddy