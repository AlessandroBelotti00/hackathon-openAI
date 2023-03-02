import pyttsx3
import keyboard
import win32clipboard
import time
import threading
import streamlit as st

engine = pyttsx3.init()
stop_flag = threading.Event()


def stopSpeach():
    stop_flag.set()
    st.write("dopo set flag")

def init(string):
    # Inizializza l'engine TTS
    voices = engine.getProperty('voices')

    # Imposta la velocità di lettura
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)

    # funzione che esegue la riproduzione della voce
    def play_voice(string):
        # fai leggere il testo
        engine.say(string)
        # avvia la riproduzione del suono
        engine.runAndWait()

    # esegui la riproduzione della voce in un thread separato
    thread = threading.Thread(target=play_voice, args=(string,))
    thread.start()

    # aspetta l'evento di interruzione
    while True:
        if stop_flag.is_set():
            st.write("dentro stop_flag.is_set()")
            # imposta il flag per interrompere la riproduzione
            stop_flag.clear()
            # interrompi la riproduzione
            engine.stop()
            break

    # attendo che il thread termini
    thread.join()




def onWord(name, location, length):
    print ('word', name, location, length)
    if keyboard.is_pressed("esc"):
       engine.stop()


""" 
def read_text(string):
    # Inizializza l'engine TTS
    voices = engine.getProperty('voices')

    # Imposta la velocità di lettura
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)

    
    

    # Legge il testo
    #engine.say(string)


    # Aspetta che la lettura sia completata
    #engine.runAndWait()
    
    words = string.split(" ")
    for i in words:
        engine.say(i)
        engine.runAndWait()
        if keyboard.is_pressed("esc"):
            engine.stop()

def on_key_press(event):
    if event.name == 'p':
        # controlla se il motore TTS sta riproducendo un suono
        if engine.isBusy():
            # se è in riproduzione, mettilo in pausa
            engine.pause()
        else:
            # altrimenti, riprendi la riproduzione
            engine.runAndWait()
 """