import speech_recognition as sr

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        ask = r.recognize_google(audio, language='en-us')
        print(f"You said : {ask}")
    except Exception:
        print("Say that again please...")
        return ""
    return ask

command()
