from faster_whisper import WhisperModel
import os

# Load Whisper Model
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def transcribe_audio(audio_path: str):

    if not os.path.exists(audio_path):
        raise FileNotFoundError(
            f"Audio file not found: {audio_path}"
        )

    segments, info = model.transcribe(
        audio_path,
        task="transcribe",
        beam_size=5
    )

    detected_text = ""

    for segment in segments:
        detected_text += segment.text + " "

    return {
        "detected_language": info.language,
        "language_probability": info.language_probability,
        "text": detected_text.strip()
    }