from voiceid.sr import Voiceid
from voiceid.db import GMMVoiceDB
import sys

#   create voice db

db = GMMVoiceDB('voiceDB')

print "DB Models:"
print db.get_speakers()

v = Voiceid(db, sys.argv[1])

v.extract_speakers(False, True)

# Set cluster speaker
c = v.get_cluster('S1')
c.set_speaker('derek')

c = v.get_cluster('S6')
c.set_speaker('derek')

# update db
v.update_db()
print "DB Models:"
print db.get_speakers()
