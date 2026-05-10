from fastapi import APIRouter
from app.models.request_models import TranslationRequest
from app.services.translation_service import translate_text

router = APIRouter(
    prefix="/translate",
    tags=["Translation"]
)

@router.post("/")
def translate(request: TranslationRequest):

    translated_text = translate_text(
        request.text,
        request.source_lang,
        request.target_lang
    )

    return {
        "original_text": request.text,
        "translated_text": translated_text
    }