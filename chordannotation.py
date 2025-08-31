import music21
def annotatechords(a,style="numeral",cdf=False,freq=-1):
    b=a.chordify()
    if cdf:
        match style:
            case "root":
                for i in b.recurse().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and i.offset%freq==0) or freq==-1 or (freq==0 and i.offset==0):
                        i.addLyric(str(i.root().name))
            case "commonname":
                for i in b.recurse().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and i.offset%freq==0) or freq==-1 or (freq==0 and i.offset==0):
                        i.addLyric(str(i.commonName))
            case "root+commonname":
                for i in b.recurse().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and i.offset%freq==0) or freq==-1 or (freq==0 and i.offset==0):
                        i.addLyric(str(i.root().name)+" "+str(i.commonName))
            case "numeral":
                for i in b.recurse().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and i.offset%freq==0) or freq==-1 or (freq==0 and i.offset==0):
                        i.addLyric(str(music21.roman.romanNumeralFromChord(i,a.analyze('key')).figure))
            case _:
                raise TypeError
        return b
    
    else:
        ln=b.recurse().getElementsByClass(music21.meter.TimeSignature)[0].numerator
        match style:
            case "root":
                for i in b.flatten().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and (0.125*round(i.offset/.125))%1==0) or freq==-1 or (freq==0 and i.offset%ln==0):
                        i.addLyric(str(i.root().name))
                        if i.lyrics:
                            a.flatten().getElementsByOffset((0.125*round(i.offset/.125)),mustBeginInSpan=False).notesAndRests[0].addLyric(i.lyric)
            case "commonname":
                for i in b.flatten().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and (0.125*round(i.offset/.125))%1==0) or freq==-1 or (freq==0 and i.offset%ln==0):
                        i.addLyric(str(i.commonName))
                        if i.lyrics:
                            a.flatten().getElementsByOffset((0.125*round(i.offset/.125)),mustBeginInSpan=False).notesAndRests[0].addLyric(i.lyric)
            case "root+commonname":
                for i in b.flatten().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and (0.125*round(i.offset/.125))%1==0) or freq==-1 or (freq==0 and i.offset%ln==0):
                        i.addLyric(str(i.root().name)+" "+str(i.commonName))
                        if i.lyrics:
                            a.flatten().getElementsByOffset((0.125*round(i.offset/.125)),mustBeginInSpan=False).notesAndRests[0].addLyric(i.lyric)
            case "numeral":
                for i in b.flatten().getElementsByClass(music21.chord.Chord):
                    if (freq==1 and (0.125*round(i.offset/.125))%1==0) or freq==-1 or (freq==0 and i.offset%ln==0):
                        i.addLyric(str(music21.roman.romanNumeralFromChord(i,a.analyze('key')).figure))
                        if i.lyrics:
                            a.flatten().getElementsByOffset((0.125*round(i.offset/.125)),mustBeginInSpan=False).notesAndRests[0].addLyric(i.lyric)
            case _:
                raise TypeError   
        return a
    


