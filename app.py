import streamlit as st
from pydub import AudioSegment
from aift.multimodal import textqa
from aift import setting
import requests
import json
from io import BytesIO

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
    }
    div[data-testid="stVerticalBlock"] > div:nth-of-type(1) {
        background-color: #87CEEB;
        padding: 10px;
        border-radius: 5px;
    }
    div[data-testid="stVerticalBlock"] > div:nth-of-type(2) {
        background-color: #FFC0CB;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

setting.set_api_key('T69FqnYgOdreO5G0nZaM8gHcjo1sifyU')

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        "<h1 style='text-align: center; font-family: Times New Roman;'>Choose Your Country</h1>",
        unsafe_allow_html=True
    )
    col4, col5, col6 = st.columns(3)

    country = None
    if st.button("ประเทศไทย (ภาษากลาง)", use_container_width=True):
        country = "Thailand"
    elif st.button("English", use_container_width=True):
        country = "English"
    elif st.button("Chinese", use_container_width=True):
        country = "Chinese"

with col2:
    st.markdown("<h1 style='text-align: center;'>เลือกภาษาถิ่น</h1>", unsafe_allow_html=True)

    land = ["< โปรดเลือกภาษาถิ่นของคุณ >", "อีสาน", "เหนือ", "ใต้"]
    selected_region = st.selectbox("Select Region:", land, index=0)

    region_ports = {
        "อีสาน": 27020,
        "เหนือ": 27021,
        "ใต้": 27022
    }

    def text_to_speech(text, speaker=1, language="th", volume=1, speed=1):
        url = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
        payload = {
            "text": text,
            "speaker": speaker,
            "volume": volume,
            "speed": speed,
            "type_media": "mp3",
            "save_file": "false",
            "language": language
        }
        headers = {
            'Botnoi-Token': 'ZHBaNlR4WEI3dWgyZGVRajRMaGt5S3NXeUVZMjU2MTg5NA==',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            audio_url = data.get("audio_url")
            if audio_url:
                audio_response = requests.get(audio_url)
                audio_response.raise_for_status()
                return BytesIO(audio_response.content)
            else:
                st.error("Audio URL not found in the response.")
                return None
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
            return None

    audio_value = st.audio_input("Record a voice message", key=2)

    if audio_value is not None:
        st.audio(audio_value)
        audio_bytes = audio_value.getvalue()
        audio = AudioSegment.from_wav(BytesIO(audio_bytes))
        audio = audio.set_frame_rate(16000).set_channels(1)
        output_audio = BytesIO()
        audio.export(output_audio, format="wav")
        output_audio.seek(0)

        st.success("Audio processed successfully.")

        if country == "English":
            transcript = textqa.generate("Please transcribe this audio in English.", return_json=False)
            st.write(f"Transcript: {transcript}")

            answer = textqa.generate(f'{selected_region} คำว่า "{transcript}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)
            translated_audio = text_to_speech(answer, speaker=100, language="en")
            if translated_audio:
                st.audio(translated_audio, format="audio/mp3")

        elif country == "Chinese":
            transcript = textqa.generate("Please transcribe this audio in Chinese.", return_json=False)
            st.write(f"Transcript: {transcript}")

            answer = textqa.generate(f'{selected_region} คำว่า "{transcript}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)
            translated_audio = text_to_speech(answer, speaker=60, language="zh")
            if translated_audio:
                st.audio(translated_audio, format="audio/mp3")

        elif country == "Thailand":
            transcript = textqa.generate("Please transcribe this audio in Thai.", return_json=False)
            st.write(f"Transcript: {transcript}")

            answer = textqa.generate(f'{selected_region} คำว่า "{transcript}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)
            translated_audio = text_to_speech(answer, speaker=6, language="th")
            if translated_audio:
                st.audio(translated_audio, format="audio/mp3")

    else:
        st.warning("Please select your dialect before recording.")
