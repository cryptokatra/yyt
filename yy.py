import streamlit as st
from pytube import YouTube

# set Chinese language
st.set_page_config(page_title="YouTube下載器", page_icon=":guardsman:", layout="wide")

# create search box
search_box = st.sidebar.text_input("輸入YouTube鏈接")

if search_box:
    # create pytube YouTube object based on the link entered
    yt = YouTube(search_box)
    
    # get video information
    title = yt.title
    thumbnail = yt.thumbnail_url
    duration = yt.length
    
    # display video information
    st.write(f"標題：{title}")
    st.image(thumbnail, width=200)
    st.write(f"影片時長：{duration} 秒")
    
    # display download options
    st.write("影片下載：")
    for stream in yt.streams.filter(progressive=True):
        st.write(f"{stream.resolution} - {stream.filesize} - " +
                 f"[下載]({stream.download()})")
    st.write("音頻下載：")
    for stream in yt.streams.filter(only_audio=True):
        st.write(f"{stream.abr} - {stream.filesize} - " +
                 f"[下載]({stream.download()})")
