import subprocess
from voiceid.sr import Voiceid
from voiceid.db import GMMVoiceDB
import sys
import speech_recognition as sr

fileStorage = sys.argv[1]

subprocess.check_output(["python", "speak.py", fileStorage]);

#   create voice db

db = GMMVoiceDB('voiceDB')

print "DB Models:"
print db.get_speakers()
print

v = Voiceid(db, sys.argv[1])

v.extract_speakers(False, True, True)
# print "\nSpeakers:\n"
speakerName = "unknown"

for c in v.get_clusters():
    cluster = v.get_cluster(c)
    distance = cluster.get_distance()
    speakerPrinted = False
    # print distance
    # print cluster.get_best_five()
    # print

    if (cluster.get_best_speaker() != "unknown" or abs(cluster.get_best_five()[0][1]) > 34):
        # print cluster
        # print
        speakerName = cluster.get_best_speaker()
        speakerPrinted = True

    if (not speakerPrinted and abs(distance) >= 0.02):
        # print str(cluster.get_name()) + " (" + str(cluster.get_best_five()[0][0]) + ")"
        # print
        speakerName = cluster.get_best_five()[0][0]
        speakerPrinted = True

    if (not speakerPrinted):
        # print cluster
        # print
        speakerName = cluster.get_best_speaker()
        speakerPrinted = True

    # print str(cluster.get_name()) + " (" + str(speakerName) + ")"
    # cluster.print_segments()
    # print "===================================================="
    # print


r = sr.Recognizer()

with sr.WavFile(fileStorage) as source:
    audio = r.record(source)

try:
    # print("Transcription: " + r.recognize(audio))
    print str(speakerName) + ": " + str(r.recognize(audio))
except LookupError:
    print(str(speakerName) + ": " + "Could not understand audio")

if (speakerName == "unknown"):
    print
    print distance
    print cluster.get_best_five()
