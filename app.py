import streamlit as st
from streamlit_mic_recorder import mic_recorder

st.title("Microphone Recorder")

# Initialize the microphone recorder
audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    just_once=True,
    use_container_width=True,
    key="recorder"
)

# If audio is recorded, play it back
if audio:
    st.audio(audio['bytes'], format='audio/wav')
    st.write("Recording complete. Playback above.")
