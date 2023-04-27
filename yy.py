import streamlit as st
import pafy
import os

def download_video(url):
    video = pafy.new(url)
    title = video.title
    thumbnail = video.thumb
    duration = video.duration
    video_streams = video.streams 
    audio_streams = video.audiostreams
    video_table = []
    audio_table = []
    
    for stream in video_streams:
        if(stream.extension == "mp4"):
            size = f"{stream.get_filesize()//(1024*1024)} MB"
            quality = stream.quality
            download_link = stream.url
            video_table.append([quality,size,f"[Download]({download_link})"])
    
    for stream in audio_streams:
        size = f"{stream.get_filesize()//(1024*1024)} MB"
        quality = stream.quality
        download_link = stream.url
        audio_table.append([quality,size,f"[Download]({download_link})"])
    
    st.markdown(f"影片標題: {title}")
    st.image(thumbnail)
    st.write(f"影片時長: {duration}")
    
    st.subheader("影片下載:")
    st.table(video_table)
    
    st.subheader("音訊下載:")
    st.table(audio_table)
    
    return title, video_streams[-1].url

def main():
    st.set_page_config(page_title="Youtube Downloader", page_icon=":memo:", layout="wide")
    st.title("Youtube Downloader")
    
    url = st.text_input("請輸入Youtube影片連結:")
    
    if(url):
        if("playlist" in url):
            st.warning("不接受Youtube播放清單URL")
        else:
            try:
                title, video_link = download_video(url)
                folder_name = "downloads"
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                filename = os.path.join(folder_name,f"{title}.mp4")
                st.info(f"下載 {title}.mp4 至 {os.getcwd()}/{folder_name}")
                st.markdown(f'<a download href="{video_link}" >下載 {title}.mp4</a>',unsafe_allow_html=True)
            except ValueError:
                st.warning("無效的Youtube連結")
            except:
                st.error("下載錯誤")

if __name__ == '__main__':
    main()
