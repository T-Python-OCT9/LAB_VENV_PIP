from distutils.command.install_egg_info import to_filename
from art import text2art,tprint

hi_art=text2art("hi",font="black")#print with out print sentis
print(hi_art)
print("_"*50)
tprint("I am Alaa","random-xlarge")
print("_"*50)
tprint("the sentence for my lab is")
print("_"*50)
sentence_art=name_art=text2art("BELIEVE and ACHEIVE",font="cybermedum")
print(sentence_art)
print("_"*50)
tprint("bye","rand-xlarge")
tprint("sentence with font block",font="small")
tprint("BELIEVE and ACHEIVE",font="block")

