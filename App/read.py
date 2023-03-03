import pyttsx3

engine = pyttsx3.init()


def init(string):
    # Init TTS engine
    voices = engine.getProperty('voices')

    # Imposta la velocità di lettura
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)

    # Prepare the text to be read
    engine.say(string)
    # Start to speak
    engine.runAndWait()