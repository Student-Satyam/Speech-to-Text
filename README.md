🎤 Speech-to-Text App (Whisper)

A fast and reliable Speech-to-Text web app built with Streamlit and Faster-Whisper.
Upload any .mp3 or .wav file and get high-quality transcription instantly — fully compatible with Streamlit Cloud (no FFmpeg required).

🚀 Features

Upload audio files (.mp3, .wav)

Fast, accurate transcription

Works on CPU-only environments (Streamlit Cloud)

No FFmpeg installation needed

Clean, simple Streamlit UI

🛠️ Requirements

requirements.txt

streamlit
faster-whisper
numpy
torch

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

📁 Project Structure
speech-to-text/
├── app.py
├── requirements.txt
└── README.md

🧠 How It Works

User uploads audio

App saves it to a temporary file

Faster-Whisper transcribes the audio using the CPU

Transcription is displayed in the browser

🧪 Core Code Snippet
from faster_whisper import WhisperModel
import streamlit as st
import tempfile, os

@st.cache_resource
def load_whisper_model():
    return WhisperModel("base", device="cpu")

model = load_whisper_model()

audio = st.file_uploader("Upload audio", type=["mp3","wav"])
if st.button("Transcribe") and audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio.getvalue())
        path = tmp.name
    segments, _ = model.transcribe(path)
    text = " ".join([s.text for s in segments])
    st.write(text)
    os.remove(path)

🌐 Deploy on Streamlit Cloud

Push your project to GitHub

Go to https://streamlit.io/cloud

Select your repository

Deploy — done!

Streamlit Cloud installs everything automatically.

📄 License

MIT License — free to use and modify.
