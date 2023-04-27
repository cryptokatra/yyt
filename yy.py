import streamlit as st
import pytube
import os

# 設置網頁標題和畫面布局
st.set_page_config(page_title="YouTube Downloader", layout="wide")

# 定義下載函數
def download(url, format):
    # 解析影片
    video = pytube.YouTube(url)

    # 選擇下載的流
    if format == "Video":
        stream = video.streams.filter(file_extension='mp4', res='720p').first()
    else:
        stream = video.streams.filter(only_audio=True).first()

    # 下載影片或音頻
    stream.download()

    # 提示下載完成
    st.success('下載完成！')
    
# 定義主函數
def main():
    # 設置應用程序的標題和説明
    st.title("YouTube Downloader")
    st.write("輸入YouTube鏈接和下載格式。支持下載720p MP4視頻和音頻文件。")

    # 創建表單
    form = st.form(key='my_form')
    url = form.text_input(label='輸入YouTube鏈接')
    format = form.selectbox('下載格式', ('Video', 'Audio'))
    submit = form.form_submit_button(label='下載')

    # 下載影片或音頻
    if submit and url:
        try:
            download(url, format)
        except Exception as e:
            st.error('下載失敗：{}'.format(e))

# 運行應用程序
if __name__ == '__main__':
    main()
