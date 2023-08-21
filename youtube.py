
import os
import streamlit as st
from pytube import YouTube

if not os.path.exists('./downloads'):
    os.makedirs('./downloads')

def list_streams(video_url):
    yt = YouTube(video_url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    return streams, yt

def download_video(stream, title):
    stream.download(output_path='./downloads')
    return f'./downloads/{title}.mp4'
st.title('YouTube Video Downloader')

video_url = st.text_input('Enter YouTube Video URL:')
if video_url:
    try:
        streams, yt = list_streams(video_url)
        stream_options = [str(s) for s in streams]
        
        selected_stream = st.selectbox('Choose a video format:', stream_options)
        
        if st.button('Download Video'):
            for s in streams:
                if str(s) == selected_stream:
                    video_path = download_video(s, yt.title)
                    st.success(f"Video downloaded successfully! Path: {video_path}")
                    break
                    
    except Exception as e:
        st.error(f"An error occurred: {e}")
