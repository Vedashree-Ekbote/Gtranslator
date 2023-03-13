import tkinter
from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator

# tkinter
root = Tk()
root.title("Translator")
root.geometry("1080x600")
root.resizable(False, False)
root.configure(background="Black")


# Lable Of translator
def label_title():
    c1 = combo1.get()
    c2 = combo2.get()
    lable1.configure(text=c1)
    lable2.configure(text=c2)
    root.after(1000, label_title)


# Function for translation
def translate_text():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    transe_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    transe_text = transe_text.text
    text2.delete(1.0, END)
    text2.insert(END, transe_text)


# Image icon
image_icon = PhotoImage(file="images.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="download.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# Language
language = googletrans.LANGUAGES
languageV = list(language.values())
lang = language.keys()

# Text
combo1 = ttk.Combobox(root, values=languageV, font="roboto 15", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")
lable1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="pink", width=18, bd=5, relief=GROOVE)
lable1.place(x=25, y=50)

combo2 = ttk.Combobox(root, values=languageV, font="roboto 15", state="r")
combo2.place(x=750, y=20)
combo2.set("SELECT LANGUAGE")
lable2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="pink", width=18, bd=5, relief=GROOVE)
lable2.place(x=620, y=50)

label_title()

f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=440, height=210)
text1 = Text(f1, font="roboto 20", bg="powderblue", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scroll1 = Scrollbar(f1)
scroll1.pack(side="right", fill='y')
scroll1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll1.set)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)
text2 = Text(f2, font="robto 20", bg="powderblue", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scroll2 = Scrollbar(f2)
scroll2.pack(side="right", fill='y')
scroll2.configure(command=text2.yview)
text2.configure(yscrollcommand=scroll2.set)

translate = Button(root, text="Translate", font=("roboto", 15), activebackground="skyblue", cursor="hand2", bd=1, width=10, height=2, bg="green", fg="yellow", command=translate_text)
translate.place(x=476, y=250)
root.mainloop()
