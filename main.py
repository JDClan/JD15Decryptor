import json
import os
import struct
# jd15 decryptor by just dance clan
# don't steal :heart:
print("JD2015 Decryptor by Just Dance Clan")
codename = input("Codename from tapes: ")
# dtape decrypting started
tape = {"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"MapName":"","SoundwichEvent":""}
dtapeinput = 'input/' + codename + '_tml_dance.dtape.ckd'
with open(dtapeinput, 'rb') as a:
    dtape = a.read()
clipscount = int(dtape[16:20].hex(), 16)
i = 0
a = 20
b = 24
while i < clipscount:
    os.system('cls')
    if (dtape[a:b].hex()) == '955384a1':
        a += 8
        b += 8
        clipid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        trackid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        isactive = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        starttime = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        duration = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        classifierlength = int(dtape[a:b].hex(), 16)
        a += 4
        b += classifierlength
        classifier = dtape[a:b].decode("utf-8")
        a += classifierlength
        b += 4
        pathlength = int(dtape[a:b].hex(), 16)
        a += 4
        b += pathlength
        path = dtape[a:b].decode("utf-8")
        classifierpath = path + classifier
        a += pathlength + 8
        b += 12
        goldmove = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        coachid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        movetype = int(dtape[a:b].hex(), 16)
        a += 84
        b += 84
        motionclip = ({
            "__class": "MotionClip",
            "Id": clipid,
            "TrackId": trackid,
            "IsActive": isactive,
            "StartTime": starttime,
            "Duration": duration,
            "ClassifierPath": classifierpath,
            "GoldMove": goldmove,
            "CoachId": coachid,
            "MoveType": movetype,
            "Color": [1, 1, 1, 1],
            "MotionPlatformSpecifics": {
                "X360": {
                    "__class": "MotionPlatformSpecific",
                    "ScoreScale": 1,
                    "ScoreSmoothing": 0,
                    "ScoringMode": 0
                },
                "ORBIS": {
                    "__class": "MotionPlatformSpecific",
                    "ScoreScale": 1,
                    "ScoreSmoothing": 0,
                    "ScoringMode": 0
                },
                "DURANGO": {
                    "__class": "MotionPlatformSpecific",
                    "ScoreScale": 1,
                    "ScoreSmoothing": 0,
                    "ScoringMode": 0
                }
            }
        })
        tape['Clips'].append(motionclip)
        i += 1
        print("DTape clips ready: " + str(i) + "/" + str(clipscount))
    elif (dtape[a:b].hex()) == '52ec8962':
        a += 8
        b += 8
        clipid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        trackid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        isactive = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        starttime = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        duration = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        pictolen = int(dtape[a:b].hex(), 16)
        a += 4
        b += pictolen
        picto = dtape[a:b].decode("utf-8")
        a += pictolen
        b += 4
        pathlen = int(dtape[a:b].hex(), 16)
        a += 4
        b += pathlen
        path = dtape[a:b].decode("utf-8")
        pictopath = path + picto
        a += pathlen + 8
        b += 12
        coachcount = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        pictogramclip = ({
            "__class": "PictogramClip",
            "Id": clipid,
            "TrackId": trackid,
            "IsActive": isactive,
            "StartTime": starttime,
            "Duration": duration,
            "PictoPath": pictopath,
            "MontagePath": "",
            "AtlIndex": coachcount,
            "CoachCount": coachcount
        })
        tape['Clips'].append(pictogramclip)
        i += 1
        print("DTape clips ready: " + str(i) + "/" + str(clipscount))
    elif (dtape[a:b].hex()) == 'fd69b110':
        a += 8
        b += 8
        clipid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        trackid = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        isactive = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        starttime = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        duration = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        effecttype = int(dtape[a:b].hex(), 16)
        a += 4
        b += 4
        goldeffectclip = ({
			"__class": "GoldEffectClip",
			"Id": clipid,
			"TrackId": trackid,
			"IsActive": isactive,
			"StartTime": starttime,
			"Duration": duration,
			"EffectType": effecttype
		})
        tape['Clips'].append(goldeffectclip)
        i += 1
        print("DTape clips ready: " + str(i) + "/" + str(clipscount))
tape['MapName'] = codename
with open('output/' + codename + '_tml_dance.dtape.ckd', "w", encoding='utf-8') as f:
      json.dump(tape, f, ensure_ascii=False)
dtapeclipscount = clipscount
print("DTape is ready!")
# dtape decrypting ended
# ktape decrypting started
tape = {"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"MapName":"","SoundwichEvent":""}
ktapeinput = 'input/' + codename + '_tml_karaoke.ktape.ckd'
with open(ktapeinput, 'rb') as a:
    ktape = a.read()
clipscount = int(ktape[16:20].hex(), 16)
i = 0
a = 20
b = 24
while i < clipscount:
    os.system('cls')
    print("DTape clips ready: " + str(dtapeclipscount) + "/" + str(dtapeclipscount))
    print("DTape is ready!")
    if (ktape[a:b].hex()) == '68552a41':
        a += 8
        b += 8
        clipid = int(ktape[a:b].hex(), 16)
        a += 4
        b += 4
        trackid = int(ktape[a:b].hex(), 16)
        a += 4
        b += 4
        isactive = int(ktape[a:b].hex(), 16)
        a += 4
        b += 4
        starttime = int(ktape[a:b].hex(), 16)
        a += 4
        b += 4
        duration = int(ktape[a:b].hex(), 16)
        a += 8
        b += 8
        lyricslength = int(ktape[a:b].hex(), 16)
        a += 4
        b += lyricslength
        lyrics = ktape[a:b].decode("utf-8")
        a += lyricslength
        b += 4
        isendofline = int(ktape[a:b].hex(), 16)
        a += 4
        b += 4
        contenttype = int(ktape[a:b].hex(), 16)
        a += 16
        b += 16
        karaokeclip = ({
            "__class": "KaraokeClip",
            "Id": clipid,
            "TrackId": trackid,
            "IsActive": isactive,
            "StartTime": starttime,
            "Duration": duration,
            "Pitch": 8.661958,
            "Lyrics": lyrics,
            "IsEndOfLine": isendofline,
            "ContentType": contenttype,
            "StartTimeTolerance": 4,
            "EndTimeTolerance": 4,
            "SemitoneTolerance": 5
        })
        tape['Clips'].append(karaokeclip)
        i += 1
    print("KTape clips ready: " + str(i) + "/" + str(clipscount))
tape['MapName'] = codename
with open('output/' + codename + '_tml_karaoke.ktape.ckd', "w", encoding='utf-8') as f:
      json.dump(tape, f, ensure_ascii=False)
ktapeclipscount = clipscount
print("KTape is ready!")
# ktape decrypting ended
# musictrack decrypting started
musictrackinput = 'input/' + codename + '_musictrack.tpl.ckd'
with open(musictrackinput, 'rb') as a:
    musictrack = a.read()
musictrack = musictrack.hex()
a = 128
b = 136
i = 0
markers = []
markerscount = int(musictrack[a:b], 16)
while i < markerscount:
    os.system('cls')
    print("DTape clips ready: " + str(dtapeclipscount) + "/" + str(dtapeclipscount))
    print("DTape is ready!")
    print("KTape clips ready: " + str(ktapeclipscount) + "/" + str(ktapeclipscount))
    print("KTape is ready!")
    a += 8
    b += 8
    marker = int(musictrack[a:b], 16)
    markers.append(marker)
    print("MusicTrack markers ready: " + str(i) + "/" + str(markerscount - 1))
    i += 1
finaljson = dict(markers = markers, startbeat = 0, endbeat = markerscount)
with open('output/' + codename + '_musictrack.json', "w", encoding='utf-8') as f:
      json.dump(finaljson, f, ensure_ascii=False)
print("MusicTrack data JSON is ready!")
print("Timelines is decrypted!")
input("Press enter to exit!")
# musictrack decrypting ended
