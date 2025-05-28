import os
from gtts import gTTS

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

while True:
    folder_name = input("Indica en que carpeta guardarás tu audió ")
    full_folder_path = os.path.join(desktop, folder_name)
    
    if os.path.isdir(full_folder_path):
        break
    
    print("La carpeta no existe. Verifica el nombre o crea la carpeta primero")
    print("Carpetas disponibles en tu ordenador")
    
    for item in os.listdir(desktop):
        item_path = os.path.join(desktop, item)
        if os.path.isdir(item_path):
            print(" -", item)
    
file_name = input("Introduce el nombre tu .txt file: ")
file_nametxt = file_name + ".txt"

try:
    with open(file_nametxt, "r", encoding="utf-8") as file:
        text = file.read()
        print("Contenido del archivo: ")
        print(text)
        
    audiofile_name = input("¿Cómo llamaras a tu archivo de audio? ")
    audiofile_nameextension = audiofile_name + ".mp3"
    folder_path = os.path.join(full_folder_path, audiofile_nameextension)
    
    tts = gTTS(text=text, lang='es')
    tts.save(folder_path)
    print(f"Audio guardado exitosamente en '{full_folder_path}' con el nombre de {audiofile_nameextension}")
    
except FileNotFoundError:
    print("No se puedo abrir el archivo. Verifica el nombre e intentalo de nuevo.")


