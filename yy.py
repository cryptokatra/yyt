import streamlit as st
from pytube import YouTube

st.title("YouTube Downloader")

# Get YouTube video URL from user
url = st.text_input("Enter YouTube video URL")

# Download video or audio
type_to_download = st.selectbox("Choose which type of file to download", ["Video", "Audio"])

# Download function
def download_video(url):
    yt = YouTube(url)

    # Get available video and audio streams
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    audio_streams = yt.streams.filter(only_audio=True)

    # Display available streams to user
    st.write("Available video streams:")
    for stream in streams:
        st.write(stream.resolution, stream.mime_type, stream.filesize)

    st.write("Available audio streams:")
    for stream in audio_streams:
        st.write(stream.abr, stream.mime_type, stream.filesize)

    # Choose stream and download
    if type_to_download == "Video":
        chosen_stream = st.selectbox("Choose video stream to download", streams)
    elif type_to_download == "Audio":
        chosen_stream = st.selectbox("Choose audio stream to download", audio_streams)

    st.write("Downloading...")
    chosen_stream.download()
    st.write("Download complete.")

# Download button
if st.button("Download"):
    if url == "":
        st.write("Please enter a URL.")
    else:
        download_video(url)
