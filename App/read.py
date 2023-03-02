import pyttsx3

def read_text(string):
    # Inizializza l'engine TTS
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Imposta la velocità di lettura
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 130)


    # Legge il testo
    engine.say(string)

    # Aspetta che la lettura sia completata
    engine.runAndWait()

