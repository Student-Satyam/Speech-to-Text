# Whisper Speech-to-Text Streamlit App

This is a simple Streamlit web application that utilizes the OpenAI Whisper model to transcribe audio files into text.

## Features
- Upload an audio file (.mp3 or .wav).
- Transcribe the audio using the Whisper 'base' model.
- Display the transcribed text.

## Setup and Installation

1.  **Clone this repository** (if applicable) or ensure `app.py` and `requirements.txt` are in your working directory.

2.  **Install the required Python packages** by running the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

3.  **FFmpeg Requirement**: The `openai-whisper` library relies on `ffmpeg` for audio processing. Ensure `ffmpeg` is installed on your system. If you're using a Colab environment, it's usually pre-installed.
    *   On Ubuntu/Debian:
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    *   On macOS (using Homebrew):
        ```bash
        brew install ffmpeg
        ```
    *   On Windows, you can download it from the official FFmpeg website and add it to your system's PATH.

## How to Run the Application

1.  **Save the Streamlit code**: Make sure you have the `app.py` file (generated previously).

2.  **Run the Streamlit app** from your terminal in the same directory as `app.py`:
    ```bash
    streamlit run app.py
    ```

3.  **For Google Colab users**: If you are running this in a Colab environment and want a public URL to share your app, use the following command:
    ```bash
    !streamlit run app.py & npx localtunnel --port 8501
    ```
    Follow the instructions provided by `localtunnel` to get your public URL.

## Usage

Once the application is running:
1.  Your web browser will open (or you'll navigate to the provided URL).
2.  You will see an option to upload an audio file.
3.  Upload your `.mp3` or `.wav` file.
4.  Click the "Transcribe Audio" button.
5.  The transcribed text will appear below.
