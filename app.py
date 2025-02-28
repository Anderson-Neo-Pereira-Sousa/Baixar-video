import yt_dlp 
import streamlit as st 

st.title("Baixar vídeos e áudios do YouTube") 
urlDoVideo = st.text_input("Digite a URL do vídeo do YouTube") 

col1, col2 = st.columns([1, 8])
with col1:
    baixarVideo = st.button("Baixar")

with col2:
    baixarAudio = st.button("Baixar apenas o áudio")

if baixarVideo and urlDoVideo:
        pasta_downloads = "downloads"
        ydl_opts = {         
                 'format': 'bv*[height=1080][ext=mp4]',         
                 'outtmpl': f'{pasta_downloads}/%(title)s.%(ext)s',     
                 }      
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([urlDoVideo])
                st.success(f"Download concluído! O vídeo foi salvo na pasta: {pasta_downloads}")

if baixarAudio and urlDoVideo:
        pasta_downloads = "downloads"
        ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{pasta_downloads}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([urlDoVideo])
                st.success(f"Download concluído! O áudio foi salvo na pasta: {pasta_downloads}")