import yt_dlp
import streamlit as st

st.title("Baixar vídeos do YouTube")
urlDoVideo = st.text_input("Digite a URL do vídeo do YouTube")
baixar = st.button("Baixar")

if baixar and urlDoVideo:
    pasta_downloads = "downloads"  # Defina o nome da pasta aqui
    ydl_opts = {
        'outtmpl': f'{pasta_downloads}/%(title)s.%(ext)s',  # Caminho para salvar o vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlDoVideo])

    st.success(f"Download concluído! O vídeo foi salvo na pasta: {pasta_downloads}")
