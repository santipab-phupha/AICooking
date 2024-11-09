import streamlit as st
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import io

st.title("Microphone Recorder")

audio = mic_recorder(
    start_prompt="Start Recording", 
    stop_prompt="Stop Recording",
    just_once=True,
    use_container_width=True,
    key="recorder"
)

if audio:
    st.write("ผ่าน 0")
    sound = AudioSegment.from_file(io.BytesIO(audio['bytes']), format="webm")
    st.write("ผ่าน 1")
    sound = sound.set_frame_rate(16000).set_channels(1)
    st.write("ผ่าน 2")
    modified_audio = io.BytesIO()
    st.write("ผ่าน 3")
    sound.export(modified_audio, format="wav")
    st.write("ผ่าน 4")
    st.audio(modified_audio.getvalue(), format='audio/wav')
    st.write("ผ่าน 5")
    st.write("Playback with frame rate set to 16000 Hz and mono channel.")
