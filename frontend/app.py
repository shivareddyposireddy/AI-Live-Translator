import streamlit as st
import tempfile
import os

from streamlit_mic_recorder import mic_recorder

from utils.api_client import (
    speech_to_text,
    translate_text,
    text_to_speech
)

st.set_page_config(
    page_title="AI Live Translator",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#4CAF50;'>
        🌍 AI Live Translator
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    "Real-time multilingual communication system"
)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn"
}

source_language = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

st.subheader("🎤 Speak Now")

audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    just_once=True
)

if audio:

    # Save audio temporarily
    temp_audio = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_audio.write(audio["bytes"])

    temp_audio.close()

    st.success("Recording completed")

    st.audio(audio["bytes"])

    # Speech Recognition
    st.info("Converting speech to text...")

    speech_result = speech_to_text(
        open(temp_audio.name, "rb")
    )

    original_text = speech_result["text"]

    st.text_area(
        "Detected Speech",
        original_text,
        height=120
    )

    # Translation
    st.info("Translating text...")

    translation_result = translate_text(
        original_text,
        languages[source_language],
        languages[target_language]
    )

    translated_text = translation_result[
        "translated_text"
    ]

    st.text_area(
        "Translated Output",
        translated_text,
        height=120
    )

    # Text To Speech
    st.info("Generating translated voice...")

    tts_result = text_to_speech(
        translated_text,
        languages[target_language]
    )

    audio_path = tts_result["audio_file"]

    if os.path.exists(audio_path):

        st.subheader("🔊 Translated Voice")

        with open(audio_path, "rb") as audio_file:

            st.audio(
                audio_file.read(),
                format="audio/mp3"
            )

    # Cleanup temp file
    os.remove(temp_audio.name)