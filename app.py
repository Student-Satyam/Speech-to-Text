import streamlit as st
from faster_whisper import WhisperModel
import tempfile
import os

@st.cache_resource
def load_whisper_model():
    return WhisperModel("base", device="cpu")

st.title("AI Demos: Whisper (Speech to Text)")

model = load_whisper_model()

audio_file = st.file_uploader("Upload audio (.mp3, .wav)", type=["mp3", "wav"])

if st.button("Transcribe Audio"):
    if audio_file:
        with st.spinner("Transcribing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_file.getvalue())
                tmp_path = tmp.name

            segments, info = model.transcribe(tmp_path)
            text = " ".join([s.text for s in segments])

            st.success("Transcribed Text:")
            st.write(text)

            os.remove(tmp_path)
    else:
        st.warning("Please upload audio first.")
