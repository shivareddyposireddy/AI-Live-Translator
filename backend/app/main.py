from fastapi import FastAPI
from app.routes import speech, translate, tts

app = FastAPI()

app.include_router(speech.router)
app.include_router(translate.router)
app.include_router(tts.router)

@app.get("/")
def home():
    return {
        "message": "AI Live Translator Backend Running"
    }