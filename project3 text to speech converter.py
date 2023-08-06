# method 1.....................


from gtts import gTTS

import os
text=open('demo.txt','r').read()

language='en'

output=gTTS(text=text,lang=language,slow=False)
output.save("fiileoutput.mp3")
os.system('start fileoutput.mp3')



# method 2.....................


import pyttsx3
text_speech=pyttsx3.init()

answer=open("demo.txt",'r').read() #(or you can enter\\ answer=input("enter which text you want to read"))
text_speech.say(answer)
text_speech.runAndWait()



# method 3................. 




from gtts import gTTS
import os 
from tkinter import *

root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

def textTospeech():
    text=entry.get()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save('ouput.mp3')
    os.system("start output.mp3")

entry=Entry(root)
canvas.create_window(200,180,window=entry)

button=Button(text="Start ",command=textTospeech)
canvas.create_window(200,230,window=button)

root.mainloop()