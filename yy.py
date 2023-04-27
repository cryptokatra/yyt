import streamlit as st
import youtube_dl

def download(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    st.success('下載完成！')

def main():
    st.title("YouTube Downloader")
    st.write("輸入YouTube鏈接，支持下載720p以下的視頻。")

    form = st.form(key='my_form')
    url = form.text_input(label='輸入YouTube鏈接')
    submit = form.form_submit_button(label='下載')

    if submit and url:
        try:
            download(url)
        except Exception as e:
            st.error('下載失敗：{}'.format(e))

if __name__ == '__main__':
    main()
