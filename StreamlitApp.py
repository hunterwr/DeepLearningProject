import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Transformer class to capture a snapshot
class SnapshotTransformer(VideoTransformerBase):
    def __init__(self):
        self.snapshot = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        if st.button("Take Picture"):
            self.snapshot = img
        return img

# Streamlit app layout
st.title("Camera Snapshot App")
st.write("Click the button to take a picture")

# Initialize the webcam streamer
ctx = webrtc_streamer(key="snapshot", video_transformer_factory=SnapshotTransformer)

# Display the captured snapshot if available
if ctx.video_transformer and ctx.video_transformer.snapshot is not None:
    st.image(ctx.video_transformer.snapshot, channels="BGR")
