import streamlit as st
import youtube_dl

# 根据给定的URL下载视频
def download_video(url):
    try:
        with youtube_dl.YoutubeDL({}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats',None)
            for f in formats:
                if f.get('format_id',None) == '22':
                    ydl.download([url])
                    return True
        return False
    except Exception as e:
        st.write("Error:", e)
        return False

# 主应用程序
def main():
    st.title("YouTube Downloader")
    st.write("Enter the YouTube URL below to download the video")
    url = st.text_input("URL")
    if st.button("Download"):
        if download_video(url):
            st.write("Downloaded Successfully!")
        else:
            st.write("Download Failed! Please Try Again.")

if __name__ == "__main__":
    main()
