import streamlit as st
from pytube import YouTube
import moviepy.editor as mp

st.title("YouTube Downloader")

# Function to download video
def download_video(video_url):
    try:
        yt = YouTube(video_url)
        st.write(f"Title: {yt.title}")
        st.write(f"Number of views: {yt.views}")
        st.write(f"Length of video: {yt.length} seconds")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        st.success("Video Downloaded Successfully")
    except Exception as e:
        st.warning("Error: Could not download video")
        st.write(e)

# Function to download audio
def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        st.write(f"Title: {yt.title}")
        st.write(f"Number of views: {yt.views}")
        st.write(f"Length of audio: {yt.length} seconds")
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        audio_file = audio.default_filename
        audio_clip = mp.AudioFileClip(audio_file)
        audio_clip.write_audiofile(f"{yt.title}.mp3")
        st.success("Audio Downloaded Successfully")
    except Exception as e:
        st.warning("Error: Could not download audio")
        st.write(e)

# Main function
def main():
    st.sidebar.title("Select Download Type")
    download_type = st.sidebar.selectbox("", ("Video", "Audio"))

    st.subheader("Enter YouTube URL")
    video_url = st.text_input("", "Paste the YouTube URL here...")

    if st.button("Download"):
        if not video_url:
            st.warning("Please enter a valid YouTube URL")
        elif download_type == "Video":
            download_video(video_url)
        elif download_type == "Audio":
            download_audio(video_url)

if __name__ == "__main__":
    main()
