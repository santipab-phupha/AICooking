import streamlit as st
from pydub import AudioSegment
from aift.multimodal import textqa
from aift import setting
import configparser
import requests
import json
import subprocess

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

setting.set_api_key('AIFT-KEYS')

# Create two columns

col1, col2= st.columns(2)


with col1:
    # Code in the left column
    st.markdown(
    "<h1 style='text-align: center; font-family: Times New Roman;'>Choose Your Country</h1>",
    unsafe_allow_html=True
    )
    col4, col5, col6 = st.columns(3)

    # Display flags in the respective columns
    list = ["thailand","english","chinese"]
    with col4:
        st.image("./Thai.jpg", use_container_width=True)
        if st.button("ประเทศไทย (ภาษากลาง)",use_container_width=True):
            config = configparser.ConfigParser()
            config.read("./config.ini")
            config["DEFAULT"]["_server_port"] = "27016"
            config["SERVER"]["_server_port"] = "27016"
            country = "Thailand"
            open("./country.txt", "w").write("Thailand")
            with open("config.ini", "w") as configfile:
                config.write(configfile)
    with col5:
        st.image("./UK.png", use_container_width=True)
        if st.button("English",use_container_width=True):
            open("./country.txt", "w").write("English")
    with col6:
        st.image("./China.png", use_container_width=True)
        if st.button("Chinese",use_container_width=True):
            country = "Chinese"
            open("./country.txt", "w").write("Chinese")

        
    # if (country := open("country.txt").read().strip()) == "English":
    #         model = whisper.load_model("tiny")
    #         audio = whisper.load_audio("./recorded_audio_en.wav")
    #         result = model.transcribe(audio)
    #         st.write(result["text"])

        # elif (country := open("country.txt").read().strip()) == "Chinese":
        # elif (country := open("country.txt").read().strip()) == "Thailand":

        

with col2:
    # Code in the left column
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Sarabun&display=swap' rel='stylesheet'><h1 style='text-align: center; font-family: Sarabun, sans-serif;'>เลือกภาษาถิ่น</h1>", unsafe_allow_html=True)

    land = ["< โปรดเลือกภาษาถิ่นของคุณ >", "อีสาน", "เหนือ", "ใต้"]
    selected_region = st.selectbox("Select Region:", land, index=0)

    region_ports = {
        "อีสาน": 27020,
        "เหนือ": 27021,
        "ใต้": 27022
    }

    def text_to_speech(text, filename="./audio_file.mp3", speaker=1, language="th", volume=1, speed=1):
        url = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
        payload = {
            "text": text,
            "speaker": speaker,
            "volume": volume,
            "speed": speed,
            "type_media": "mp3",
            "save_file": "true",
            "language": language
        }
        headers = {
            'Botnoi-Token': 'BOTNOI-AI-KEYS',
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
                with open(filename, "wb") as file:
                    file.write(audio_response.content)
                print(f"Audio downloaded successfully as '{filename}'.")
            else:
                print("Audio URL not found in the response.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    config = configparser.ConfigParser()
    config.read("./config.ini")

    new_port = str(region_ports.get(selected_region, config["DEFAULT"].get("_server_port", "27021")))
    config["DEFAULT"]["_server_port"] = new_port
    config["SERVER"]["_server_port"] = new_port

    with open("./config.ini", "w") as configfile:
        config.write(configfile)

    audio_value = st.audio_input("Record a voice message",key=2)

    if audio_value is not None:
        st.audio(audio_value)
        audio_bytes = audio_value.getvalue()
        file_path = "./recorded_audio.wav"
        with open(file_path, "wb") as file:
            file.write(audio_bytes)

        audio = AudioSegment.from_wav(file_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        output_file = "./recorded_audio.wav"
        audio.export(output_file, format="wav")

        st.success(f"Audio saved and modified as {output_file}")
        command = ["python", "partii-client-process-wav-file.py", output_file, "AIFT-KEYS"]
        result = subprocess.run(command, capture_output=True, text=True)

        output_list = [line for line in result.stdout.strip().split('\n') if line.startswith("transcript")]

        if (country := open("./country.txt").read().strip()) == "English":
            if output_list:
                speech_t = output_list[-1].replace("transcript", "").strip()
                st.write(f"Transcript: {speech_t}")

                answer = textqa.generate(f'{selected_region} คำว่า "{speech_t}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)
                
                url = "https://api.aiforthai.in.th/xiaofan-en-th/th2en"
                payload = json.dumps({"text": answer})
                headers = {
                    'apikey': 'T69FqnYgOdreO5G0nZaM8gHcjo1sifyU',
                    'Content-Type': 'application/json'
                }
                response = requests.post(url, headers=headers, data=payload)
                Outt = eval(response.text)["translated_text"]

                text_to_speech(f'{Outt}', filename="./greeting_audio.mp3", speaker=100, language="en")
                st.audio("./greeting_audio.mp3", format="audio/mp3", loop=False, autoplay=True)
            else:
                st.error("Failed to extract transcript.")

        elif (country := open("./country.txt").read().strip()) == "Chinese":
            if output_list:
                speech_t = output_list[-1].replace("transcript", "").strip()
                st.write(f"Transcript: {speech_t}")
                
                answer = textqa.generate(f'{selected_region} คำว่า "{speech_t}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)

                url = "https://api.aiforthai.in.th/xiaofan-zh-th"
                payload = json.dumps({
                "input": "ฉันจะซื้อคอมพิวเตอร์เครื่องใหม่ให้คุณ",
                "src": "th",
                "trg": "zh"
                })
                headers = {
                'apikey': 'T69FqnYgOdreO5G0nZaM8gHcjo1sifyU',
                'Content-Type': 'application/json'
                }
                
                response = requests.request("POST", url, headers=headers, data=payload)
                Outt = eval(response.text)["output"]

                text_to_speech(f'{Outt}', filename="./greeting_audio.mp3", speaker=60, language="zh")
                st.audio("./greeting_audio.mp3", format="audio/mp3", loop=False, autoplay=True)
            else:
                st.error("Failed to extract transcript.")

        elif (country := open("./country.txt").read().strip()) == "Thailand":
            if output_list:
                speech_t = output_list[-1].replace("transcript", "").strip()
                st.write(f"Transcript: {speech_t}")

                answer = textqa.generate(f'{selected_region} คำว่า "{speech_t}" แปลว่าอะไรภาษาไทย (ตอบแค่คำแปล)', return_json=False)

                text_to_speech(f'{answer}', filename="./greeting_audio.mp3", speaker=6, language="th")
                st.audio("./greeting_audio.mp3", format="audio/mp3", loop=False, autoplay=True)
            else:
                st.error("Failed to extract transcript.")

    else:
        st.warning("Please select your dialect before recording.")
