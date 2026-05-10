from fastapi import APIRouter
from app.models.request_models import TTSRequest
from app.services.text_to_speech import generate_speech

router = APIRouter(
    prefix="/tts",
    tags=["Text To Speech"]
)

@router.post("/")
def text_to_speech(
    request: TTSRequest
):

    audio_file = generate_speech(
        request.text,
        request.language
    )

    return {
        "audio_file": audio_file
    }