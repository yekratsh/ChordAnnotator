import music21
import basic_pitch.inference
from chordannotation import annotatechords
print("Welcome to ChordAnnotate, a program which uses the music21 and basic_pitch libraries to annotate chords onto a musical piece.")
result="" 
while not (result=="midi" or result=="xml" or result=="wav"):
    result=input("What filetype will you be importing? (midi, xml, or wav): ")
if result=="midi":
    print("It's recommended to only use single-track midi files. Notation errors can occur otherwise.")
fp1=input("Please input the filepath: ")
while "\\" in fp1:
    fp1=fp1.replace("\\","/")
if result=="midi" or result=="xml":
    piece=music21.converter.parse(fp1)
else:
    basic_pitch.inference.predict_and_save([fp1],fp1[:len(fp1)-(fp1[::-1].index("/")+1)],True,False,False,False,str(basic_pitch.ICASSP_2022_MODEL_PATH))
    piece=music21.converter.parse(fp1[:-4]+"_basic_pitch.mid")
result2=""
while not (result2=="1" or result2=="2" or result2=="3"):
    result2=input("How often would you like chords to be annotated? (please input number) \n1 - Once per measure \n2 - Once per beat\n3 - Annotate all possible chords\n")
if result2=="1":
    result2=0
elif result2=="2":
    result2=1
else:
    result2=-1
result3=""
while not (result3=="y" or result3=="n"):
    result3=input("Would you like the score to be chordified (notes seperated into chords)? (y/n) ")
if result3=="y":
    result3=True
else:
    result3=False
result4="" 
while not (result4=="root" or result4=="commonname" or result4=="root+commonname" or result4=="numeral"):
    result4=input("What chord notation should be used? (root/commonname/root+commonname/numeral) ")
print("Working...")
fin=annotatechords(piece,result4,result3,result2)
z=music21.musicxml.m21ToXml.GeneralObjectExporter().fromScore(fin)
fp2=input("Where should the output be stored? (filepath and name for .xml output) ")
z.write("musicxml",fp=fp2)
print("Done!")



