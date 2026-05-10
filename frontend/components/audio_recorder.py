import tempfile
from streamlit_mic_recorder import mic_recorder
import streamlit as st


def record_audio():

    st.subheader("🎤 Speak Now")

    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        just_once=True
    )

    if audio:

        temp_audio = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        temp_audio.write(audio["bytes"])

        temp_audio.close()

        st.audio(audio["bytes"])

        return temp_audio.name

    return None