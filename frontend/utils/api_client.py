import requests

BASE_URL = "https://ai-live-translator.onrender.com/"


def speech_to_text(audio_file):

    files = {
        "file": audio_file
    }

    response = requests.post(
        f"{BASE_URL}/speech/to-text",
        files=files
    )

    return response.json()


def translate_text(text, source_lang, target_lang):

    payload = {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }

    response = requests.post(
        f"{BASE_URL}/translate/",
        json=payload
    )

    return response.json()


def text_to_speech(text, language):

    payload = {
        "text": text,
        "language": language
    }

    response = requests.post(
        f"{BASE_URL}/tts/",
        json=payload
    )

    return response.json()
