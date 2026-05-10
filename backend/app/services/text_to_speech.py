from gtts import gTTS
import uuid
import os

OUTPUT_DIR = "generated_audio"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

def generate_speech(
    text,
    language
):

    file_name = f"{uuid.uuid4()}.mp3"

    file_path = os.path.join(
        OUTPUT_DIR,
        file_name
    )

    tts = gTTS(
        text=text,
        lang=language,
        slow=False
    )

    tts.save(file_path)

    return file_path