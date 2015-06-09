import speech_recognition as sr
import sys

r = sr.Recognizer()

with sr.WavFile(sys.argv[1]) as source:
    audio = r.record(source)

# with sr.Microphone() as source:
#     audio = r.listen(source)

try:
    print("Transcription: " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")
