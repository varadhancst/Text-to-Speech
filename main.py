from playsound import playsound
from tkinter import *
import tkinter as tk
from text_to_speech import speak
from tkinter import messagebox
from tkinter import filedialog
import PyPDF2

# speak(text, "ta", save=True, file="Hello-World.mp3", speak=True)
# in english if you want hear on realtime give speak=True otherwise choose false
# speak(text, "en", save=True, file=f"default.mp3", speak=False)

root = Tk()
root.title('Text to speech')
root.geometry("800x800")


def quit_app():
    root.destroy()


def play():
    playsound('default.mp3')


def open_pdf_to_convert():
    file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
    if file:
        pdf_file = PyPDF2.PdfFileReader(file)
        page = pdf_file.getPage(0)
        content = page.extractText()
        textbox.insert(1.0, content)


def convert_pdf_to_audio():
    text = textbox.get(1.0, tk.END)
    if len(text) > 1:
        open_pdf.destroy()
        upload_info.destroy()
        close_button.destroy()
        submit_button.destroy()
        speak(text, "en", save=True, file=f"default.mp3", speak=False)
        play_button = Button(root, text="Play text", font=("Helvetica", 32), relief=GROOVE, command=play)
        play_button.pack(pady=20)

        info = Label(root, text="Click on the button above to play speech ", font=("times new roman", 10, "bold"))
        info.pack(pady=20)

        close_button_internal = Button(root, text="Close window", font=("Helvetica", 25), relief=GROOVE,
                                       command=quit_app)
        close_button_internal.pack(pady=20)
    else:
        messagebox.showwarning("Warning", "please enter some words")


title = Label(root, text="Text to Speech", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="white",
              fg="green")
title.pack(side=TOP, fill=X)

open_pdf = Button(root, text="Upload file", font=("Helvetica", 32), relief=GROOVE, command=open_pdf_to_convert)
open_pdf.pack(pady=20)

upload_info = Label(root, text="Upload a pdf file or write in a below textbox", font=("times new roman", 10, "bold"))
upload_info.pack(pady=20)

textbox = Text(height=5, width=80, font=("times new roman", 20, "bold"))
textbox.pack(pady=20)

submit_button = Button(root, text="Submit", font=("Helvetica", 32), relief=GROOVE, command=convert_pdf_to_audio)
submit_button.pack(pady=20)

close_button = Button(root, text="Close window", font=("Helvetica", 32), relief=GROOVE, command=quit_app)
close_button.pack(pady=20)

root.mainloop()
