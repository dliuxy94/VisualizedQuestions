from voiceid.sr import Voiceid
from voiceid.db import GMMVoiceDB
from os import listdir
from os.path import isfile, join, splitext
import sys
import os

directory = sys.argv[1]

onlyfiles = [ f for f in listdir(directory) if isfile(join(directory,f)) and splitext(f)[1] == ".wav" ]

db = GMMVoiceDB('voiceDB');

print db.get_speakers()

for f in onlyfiles:
    print "adding: " + f
    basename = os.path.abspath('./trainAudio/' + splitext(f)[0])
    db.add_model(basename, splitext(f)[0]) # add_model need to take in filepath without extension to work

print db.get_speakers()
