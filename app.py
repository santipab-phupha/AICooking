import streamlit as st
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
from aift.multimodal import textqa
from aift import setting
import configparser
import requests
import json
import os
import subprocess

setting.set_api_key('T69FqnYgOdreO5G0nZaM8gHcjo1sifyU')

st.title("Audio Translator and TextQA")

# Region selection dropdown
st.write("### Step 1: Select your dialect")
land = ["โปรดเลือกภาษาถิ่นของคุณ", "อีสาน", "เหนือ", "ใต้"]
selected_region = st.selectbox("Select Region:", land, index=0)

# Region ports mapping
region_ports = {
    "อีสาน": 27020,
    "เหนือ": 27021,
    "ใต้": 27022
}

config = configparser.ConfigParser()
config.read("config.ini")

new_port = str(region_ports.get(selected_region, config["DEFAULT"].get("_server_port", "27021")))
config["DEFAULT"]["_server_port"] = new_port
config["SERVER"]["_server_port"] = new_port

with open("config.ini", "w") as configfile:
    config.write(configfile)

st.write("### Step 2: Record your audio")
with st.spinner("Recording..."):
    audio_data = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        just_once=True,
        use_container_width=True,
        key="recorder"
    )

if audio_data:
    st.audio(audio_data['bytes'], format='audio/wav')
    st.success("Recording complete.")

    # Save recorded audio to a temporary file for processing
    temp_path = "temp_recorded.wav"
    with open(temp_path, "wb") as f:
        f.write(audio_data['bytes'])

    # Process the audio
    audio = AudioSegment.from_file(temp_path, format="wav")
    audio = audio.set_frame_rate(16000).set_channels(1)
    output_file = "temp_converted.wav"
    audio.export(output_file, format="wav")

    # Run external process to get transcript
    command = ["python", "partii-client-process-wav-file.py", output_file, "T69FqnYgOdreO5G0nZaM8gHcjo1sifyU"]
    result = subprocess.run(command, capture_output=True, text=True)

    output_list = [line for line in result.stdout.strip().split('\n') if line.startswith("transcript")]
    if output_list:
        speech_t = output_list[-1].replace("transcript", "").strip()
        st.write(f"Transcript: {speech_t}")

        # Generate answer using textqa
        answer = textqa.generate(f'{selected_region} คำว่า "{speech_t}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)

        # Translate answer to English
        url = "https://api.aiforthai.in.th/xiaofan-en-th/th2en"
        payload = json.dumps({"text": answer})
        headers = {
            'apikey': 'T69FqnYgOdreO5G0nZaM8gHcjo1sifyU',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        Outt = eval(response.text)["translated_text"]
        st.write(f'Translated Answer: {Outt}')
    else:
        st.error("Failed to extract transcript.")

    # Clean up temporary files
    os.remove(temp_path)
    os.remove(output_file)
else:
    st.warning("Please select your dialect before recording.")
