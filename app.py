import streamlit as st
import os
import whisper
import tempfile
import numpy as np

@st.cache_resource
def load_whisper_model():
    # Note: You might need to install 'ffmpeg' on your system for Whisper to work.
    # For Colab, it's usually pre-installed or handled by the whisper library.
    model = whisper.load_model("base")
    return model

# --- Streamlit App --- 
st.title("AI Demos: Whisper (Speech to Text)")

st.header("Whisper (Speech to Text)")
whisper_model = load_whisper_model()

audio_file = st.file_uploader("Upload an audio file (.mp3, .wav)", type=["mp3", "wav"])

if st.button("Transcribe Audio"):
    if audio_file is not None:
        with st.spinner("Transcribing audio..."):
            # Save the uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix="." + audio_file.name.split('.')[-1]) as tmp_file:
                tmp_file.write(audio_file.getvalue())
                tmp_file_path = tmp_file.name

            try:
                result = whisper_model.transcribe(tmp_file_path)
                st.success("Transcribed Text:")
                st.write(result["text"])
            except Exception as e:
                st.error(f"Error during transcription: {e}")
            finally:
                # Clean up the temporary file
                os.remove(tmp_file_path)
    else:
        st.warning("Please upload an audio file first.")
