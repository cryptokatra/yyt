import streamlit as st
import youtube_dl

st.set_page_config(page_title="YouTube下載器", page_icon=":guardsman:", layout="wide")

# create search box
search_box = st.sidebar.text_input("輸入YouTube鏈接")

if search_box:
    with youtube_dl.YoutubeDL() as ydl:
        # get video information
        video = ydl.extract_info(search_box, download=False)
        title = video['title']
        thumbnail = video['thumbnail']
        duration = video['duration']
        formats = video['formats']

        # display video information
        st.write(f"標題：{title}")
        st.image(thumbnail, width=200)
        st.write(f"影片時長：{duration} 秒")

        # display download options
        st.write("影片下載：")
        for f in formats:
            if f['format_note'] == '1080p':
                st.write(f"{f['format_note']} - {f['filesize'] / 1048576:.2f}MB - " +
                         f"[下載]({f['url']})")
        
        st.write("音訊下載：")
        for f in formats:
            if f['format_note'] == 'audio only':
                st.write(f"{f['acodec']} - {f['filesize'] / 1048576:.2f}MB - " +
                         f"[下載]({f['url']})")
