from utils.api_client import (
    speech_to_text,
    translate_text
)


def process_translation(
    audio_path,
    source_lang,
    target_lang
):

    # Speech Recognition
    speech_result = speech_to_text(
        open(audio_path, "rb")
    )

    original_text = speech_result["text"]

    # Translation
    translation_result = translate_text(
        original_text,
        source_lang,
        target_lang
    )

    translated_text = translation_result[
        "translated_text"
    ]

    return {
        "original_text": original_text,
        "translated_text": translated_text
    }