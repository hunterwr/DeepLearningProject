import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoTransformerBase


# Transformer class to capture a snapshot
class SnapshotTransformer(VideoTransformerBase):
    def __init__(self):
        self.snapshot = None  # Initialize snapshot attribute

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert the frame to a numpy array (BGR format)
        # Button to capture snapshot
        if st.button("Take Picture"):
            self.snapshot = img
        return img

# Streamlit app layout
st.title("Camera Snapshot App")
st.write("Click the button to take a picture")

# Set up RTC configuration for WebRTC connection
rtc_configuration = RTCConfiguration({
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

# Initialize the webcam streamer
ctx = webrtc_streamer(key="snapshot", rtc_configuration=rtc_configuration, video_processor_factory=SnapshotTransformer)

# Display the captured snapshot if available
if ctx.video_processor and ctx.video_processor.snapshot is not None:
    st.image(ctx.video_processor.snapshot, channels="BGR")
