import pyttsx3

def read(string):
    # Inizializza l'engine TTS
    engine = pyttsx3.init()

    # Imposta la velocità di lettura
    engine.setProperty('rate', 150)

    # Legge il testo
    engine.say(string)

    # Aspetta che la lettura sia completata
    engine.runAndWait()

