from voiceid.sr import Voiceid
from voiceid.db import GMMVoiceDB
import sys
import speech_recognition as sr

#   create voice db

db = GMMVoiceDB('voiceDB')

print "DB Models:"
print db.get_speakers()

v = Voiceid(db, sys.argv[1])

v.extract_speakers(False, True)
print "\nSpeakers:\n"

for c in v.get_clusters():
    cluster = v.get_cluster(c)
    distance = cluster.get_distance()
    speakerPrinted = False

    if (cluster.get_best_speaker() != "unknown" or abs(cluster.get_best_five()[0][1]) > 33):
        print cluster
        print
        speakerPrinted = True

    if (not speakerPrinted and abs(distance) >= 0.1):
        print str(cluster.get_name()) + " (" + str(cluster.get_best_five()[0][0]) + ")"
        print
        speakerPrinted = True

    if (not speakerPrinted):
        print cluster
        print
        speakerPrinted = True

    cluster.print_segments()
    print "===================================================="
    print

r = sr.Recognizer()

with sr.WavFile(sys.argv[1]) as source:
    audio = r.record(source)

try:
    print("Question: " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")