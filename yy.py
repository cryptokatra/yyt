import streamlit as st
import pytube
from pytube import YouTube
import pandas as pd

st.set_page_config(page_title="YouTube Downloader", page_icon=":computer:", layout="wide")

st.title("YouTube Downloader")
st.markdown("<h3>請輸入 YouTube 影片鏈接:</h3>", unsafe_allow_html=True)

# 輸入框
url = st.text_input("請輸入鏈接：")

# 檢查輸入是否為正確的YouTube鏈接
if "youtube.com" not in url:
    st.warning("請輸入正確的 YouTube 影片鏈接！")
    st.stop()

# 取得影片資訊
try:
    video = YouTube(url)
    title = video.title
    thumbnail = video.thumbnail_url
    length = video.length
    streams = video.streams
except:
    st.warning("無法取得 YouTube 影片資訊！")
    st.stop()

# 顯示影片資訊
st.subheader("影片資訊")
st.write("標題：", title)
st.image(thumbnail, width=220)
st.write("影片長度：", length, "秒")

# 下載影片
st.subheader("影片下載")
videos = streams.filter(mime_type="video/mp4").all()

if videos:
    st.write("以下是可供下載的影片：")
    video_quality = []
    video_size = []
    video_download = []
    for v in videos:
        video_quality.append(v.resolution)
        video_size.append(round(v.filesize / (1024 * 1024), 2))
        video_download.append(v)
    df_video = pd.DataFrame({"品質": video_quality, "檔案大小（MB）": video_size, "下載": video_download})
    st.write(df_video)
    
    # 下載按鈕
    for i, row in df_video.iterrows():
        if st.button(row["品質"]):
            st.write("開始下載", row["品質"], "品質的影片...")
            row["下載"].download(filename=title + ".mp4")
            st.write("影片下載完成！")

# 下載音頻
audios = streams.filter(only_audio=True).all()

if audios:
    st.write("以下是可供下載的音頻：")
    audio_quality = []
    audio_size = []
    audio_download = []
    for a in audios:
        audio_quality.append(a.abr)
        audio_size.append(round(a.filesize / (1024 * 1024), 2))
        audio_download.append(a)
    df_audio = pd.DataFrame({"品質": audio_quality, "檔案大小（MB）": audio_size, "下載": audio_download})
    st.write(df_audio)
    
    # 下載按鈕
    for i, row in df_audio.iterrows():
        if st.button(row["品質"]):
            st.write("開始下載", row["品質"], "品質的音頻...")
            row["下載"].download(filename=title + ".mp3")
            st.write("音頻下載完成！")
