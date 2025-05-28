import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="SmartSpeech", layout="centered")

st.title("🗣️ SmartSpeech - Texto a Voz")
st.write("Convierte texto escrito o archivos `.txt` en audio MP3 🎧")

# Opción 1: Escribir texto directamente
text_input = st.text_area("✍️ Escribe tu texto aquí:", height=200)

# Opción 2: Subir archivo .txt
uploaded_file = st.file_uploader("📄 ...O sube un archivo .txt", type=["txt"])

text = ""

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
elif text_input.strip() != "":
    text = text_input.strip()

# Mostrar contenido detectado
if text:
    st.success("✅ Texto listo para convertir:")
    st.write(text)

    filename = st.text_input("🧾 Nombre para el archivo MP3 (sin '.mp3')", "mi_audio")

    if st.button("🎙️ Generar MP3"):
        tts = gTTS(text, lang='es')
        tts.save(f"{filename}.mp3")

        with open(f"{filename}.mp3", "rb") as f:
            st.download_button("⬇️ Descargar MP3", f, file_name=f"{filename}.mp3")
else:
    st.info("✏️ Escribe texto o sube un archivo para comenzar.")