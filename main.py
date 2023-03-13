import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import googletrans
import pyttsx3
import speech_recognition as s_r
from googletrans import Translator

root = Tk()
root.title('translator')
root.geometry('900x450+200+200')
root.resizable(False, False)
root.configure(bg="#305065")
engine = pyttsx3.init()


def speak():
    text = text1.get(1.0, END)
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()





r = s_r.Recognizer()



def get_audio():
    
    r = s_r.Recognizer()
    my_mic_device = s_r.Microphone(device_index=1)
    with my_mic_device as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)
    return my_string


language = googletrans.LANGUAGES
languageV = list(language.values())
lang = language.keys()


def translate_text():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    transe_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    transe_text = transe_text.text
    text2.delete(1.0, END)
    text2.insert(END, transe_text)


combo1 = ttk.Combobox(root, values=languageV, width=10, height=50, font="roboto 10", state="r")
combo1.place(x=60, y=120)
combo1.set("ENGLISH")

combo2 = ttk.Combobox(root, values=languageV, width=20, height=50, font="roboto 10", state="r")
combo2.place(x=650, y=120)
combo2.set("SELECT LANGUAGE")

frame = Frame(root, width=900, height=90, bg='white')
frame.place(x=0, y=0)

Logo = PhotoImage(file='speaker logo.png')
Label(frame, image=Logo).place(x=20, y=1)
Label(frame, text="SPEECH CONVERTER", font=" Mistral 25 bold", bg="white", fg="black").place(x=200, y=20)

speak_image = PhotoImage(file="speak.png")
speak_button = Button(root, compound=CENTER, image=speak_image, width=50, command=speak)
speak_button.place(x=700, y=250)



mic_image = PhotoImage(file="images.png")
mic_button = Button(root, compound=CENTER, image=mic_image, width=50, height=100, command=get_audio)
mic_button.place(x=80, y=250)

text1 = Text(root, font="roboto 15", bg="powderblue", relief=GROOVE, wrap=WORD)
text1.place(x=30, y=150, width=200, height=75)

text2 = Text(root, font="robto 15", bg="powderblue", relief=GROOVE, wrap=WORD)
text2.place(x=650, y=150, width=200, height=75)

translate = Button(root, text="Translate", font=("roboto", 15), activebackground="skyblue", cursor="hand2", bd=1,
                   width=10, height=2, bg="green", fg="yellow", command=translate_text)
translate.place(x=400, y=250)
root.mainloop()

# gender_combobox = tkinter.ttk.Combobox(root, values=['male', 'Female'], font="arial 14", state='r', width=10)
# gender_combobox.place(X=550, Y=200)
# gender_combobox.set('male')
# speed_combobox = tkinter.ttk.Combobox(root, values=['slow', 'normal', 'fast'], font="arial 14", state='r', width=10)
# speed_combobox.place(X=730, Y=200)
# speed_combobox.set('normal')


root.mainloop()
