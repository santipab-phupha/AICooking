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

st.write("# เลือกภาษาถิ่น")
land = ["< โปรดเลือกภาษาถิ่นของคุณ >", "อีสาน", "เหนือ", "ใต้"]
selected_region = st.selectbox("Select Region:", land, index=0)

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

audio_value = st.audio_input("Record a voice message")

if audio_value is not None:

    st.audio(audio_value)
    audio_bytes = audio_value.getvalue()  
    file_path = "./recorded_audio.wav"
    with open(file_path, "wb") as file:
        file.write(audio_bytes) 
    temp_file = "./recorded_audio.wav"
    with open(temp_file, "wb") as file:
        file.write(audio_bytes)

    audio = AudioSegment.from_wav(temp_file)
    audio = audio.set_frame_rate(16000).set_channels(1)
    output_file = "recorded_audio.wav"
    audio.export(output_file, format="wav")

    st.success(f"Audio saved and modified as {output_file}")
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

else:
    st.warning("Please select your dialect before recording.")
