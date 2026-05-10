import streamlit as st
import os

from utils.api_client import text_to_speech


def play_translated_voice(
    translated_text,
    target_language
):

    tts_result = text_to_speech(
        translated_text,
        target_language
    )

    audio_path = tts_result["audio_file"]

    if os.path.exists(audio_path):

        st.subheader("🔊 Translated Voice")

        with open(audio_path, "rb") as audio_file:

            st.audio(
                audio_file.read(),
                format="audio/mp3"
            )