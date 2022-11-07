import os
from gtts import gTTS

def leer_archivo():
    #leer archivo. 
    archivo = open('texto.txt','r')
    lineas = archivo.readlines()

    for l in lineas:
        texto_a_voz(l)

def texto_a_voz(texto):

    texto = texto
    tts = gTTS(text=texto, lang='es',tld='com.mx')
    tts.save('nota.mp3')
    os.system('nota.mp3')


if __name__ == '__main__':
    leer_archivo()