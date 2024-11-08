import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
import ffmpeg
import numpy as np
import tempfile
import os
from pydub import AudioSegment

# Initialize Streamlit app
st.title("Record Video and Play Only Audio")

# Define video processor class
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        return frame

# Stream video from webcam
webrtc_ctx = webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={"video": True, "audio": True},
)

# Check if recording is done
if st.button("Stop and Extract Audio") and webrtc_ctx.state.playing:
    # Save recorded video in a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as video_file:
        video_file.write(webrtc_ctx.video_recorder.getvalue())
        video_path = video_file.name

    # Extract audio to a temporary file
    audio_path = os.path.splitext(video_path)[0] + ".mp3"
    ffmpeg.input(video_path).output(audio_path).run()

    # Load and play audio
    audio_data = AudioSegment.from_file(audio_path)
    st.audio(audio_data.export().read(), format="audio/mp3")

    # Clean up temporary files
    os.remove(video_path)
    os.remove(audio_path)
