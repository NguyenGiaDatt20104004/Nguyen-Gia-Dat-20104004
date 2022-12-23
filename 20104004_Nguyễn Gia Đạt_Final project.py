import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
import googletrans
from googletrans import Translator
from gtts import gTTS
import os
import playsound
from PIL import Image, ImageTk, ImageSequence
import speech_recognition as sr
import pytesseract
import cv2
from threading import Thread
from ttkwidgets.autocomplete import AutocompleteCombobox
import numpy as np
from PIL import ImageFont, ImageDraw, Image

root = Tk()
root.title("Auto Translator")
root.geometry("400x650+1000+30")
root.resizable(False,False)

key = list(googletrans.LANGUAGES.keys())
value = list(googletrans.LANGUAGES.values())

main_frame = Frame(root, width=400, height=650, bg="lavender")
main_frame.place(x=0, y=0)

Label(root, text="Auto Translator", font=("Times 20 bold"), fg="black", bg="lavender").pack(pady=10)
text_input = Text(main_frame, width=43, height=8, font="Times 13")
text_input.place(x=5, y=100)
text_output = Text(main_frame, width=43, height=8, font="Times 13")
text_output.place(x=5, y=300)

def translates():
    lang_1 = text_input.get("1.0", "end-1c")
    cli = choose_lang_input.get()
    clo = choose_lang_output.get()
    if lang_1 == "":
        pass
    else:
        text_output.delete(1.0, END)
        translator = Translator()
        lang_2 = translator.translate(text=lang_1, src=cli, dest=clo)
        text_output.insert("end", lang_2.text)

def clear():
    text_input.delete(1.0, END)
    text_output.delete(1.0, END)

def speak_in():
    text = text_input.get(1.0, END)
    langin = ""
    for i in range(len(list(googletrans.LANGUAGES.values()))):
        if list(googletrans.LANGUAGES.values())[i]==choose_lang_input.get():
            langin = list(googletrans.LANGUAGES.keys())[i]
    tts = gTTS(text=text, lang=langin, slow=False)
    try:
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")
    except:
        os.remove("sound.mp3")

def speak_out():
    text = text_output.get(1.0, END)
    langout = ""
    for i in range(len(list(googletrans.LANGUAGES.values()))):
        if list(googletrans.LANGUAGES.values())[i]==choose_lang_output.get():
            langout = list(googletrans.LANGUAGES.keys())[i]
    tts = gTTS(text=text, lang=langout, slow=False)
    try:
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")
    except:
        os.remove("sound.mp3")

def mic_in():
    clear()
    for i in range(len(list(googletrans.LANGUAGES.values()))):
        if list(googletrans.LANGUAGES.values())[i]==choose_lang_input.get():
            lang = list(googletrans.LANGUAGES.keys())[i]
    ear = sr.Recognizer()
    with sr.Microphone() as mic:
        ear.adjust_for_ambient_noise(mic)
        audio = ear.listen(mic)
    try:
        you = ear.recognize_google(audio, language=lang)
        text_input.insert(END, you)
    except:
        you = ""
        text_input.insert(END, you)
    translates()

def select_roi():
    file = askopenfilename(filetypes = [('All Files','*.*'),('JPG Files','*.jpg'),('PNG Files','*.png')])
    try:
        img_in = cv2.imread(file)
        roi = cv2.selectROI(img_in)
        imCrop = img_in[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        if len(imCrop)>0:
            image = Image.fromarray(cv2.cvtColor(imCrop, cv2.COLOR_BGR2RGB))
        cv2.destroyAllWindows()
        text = image_to_text(image)
        clear()
        text_input.insert(END, text)
        translates()
    except:
        pass

def openfile():
    thread = Thread(target=select_roi, daemon=True)
    thread.start()

def image_to_text(img):
    for i in range(len(list(googletrans.LANGUAGES.values()))):
        if list(googletrans.LANGUAGES.values())[i]==choose_lang_input.get():
            lang = list(googletrans.LANGUAGES.keys())[i]
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img, lang=lang)
    return text

def radio_to_text():
    file = askopenfilename(filetypes = [('All Files','*.*'),('WAV Files','*.wav'),('Mp3 Files','*.mp3')])
    try:
        try:
            r = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=choose_lang_input.get())
        except:
            pass
        clear()
        text_input.insert(END, text)
        translates()
    except:
        pass

def camera_realtime():
    for i in range(len(list(googletrans.LANGUAGES.values()))):
        if list(googletrans.LANGUAGES.values())[i]==choose_lang_input.get():
            lang = list(googletrans.LANGUAGES.keys())[i]
    translator = Translator()
    camera=cv2.VideoCapture(0)
    camera.set(3,640)
    camera.set(4,480)

    while True:
        _, frame = camera.read()
        cv2.imshow('Detect text',frame)

        #Bấm "s" để chụp
        if cv2.waitKey(1) & 0xFF == ord("s"):
            path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

            cv2.imwrite("anhchup.jpg", frame)
            camera.release()
            cv2.destroyAllWindows()
            try:
                img_in = cv2.imread("anhchup.jpg")
                roi = cv2.selectROI(img_in)
                imCrop = img_in[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
#                if len(imCrop)>0:
#                    image = Image.fromarray(cv2.cvtColor(imCrop, cv2.COLOR_BGR2RGB))         
                cv2.imwrite("anhcat.jpg", imCrop)
                cv2.destroyAllWindows()

                image = cv2.imread("anhcat.jpg")
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                boxes = pytesseract.image_to_data(image, lang=lang)
                boxes1 = image_to_text(image)
                a = boxes1.split("\n")
                q = 0
                list_translated = []
                
                for text in a:
                    try:
                        translated_text = translator.translate(text, src=choose_lang_input.get(), dest=choose_lang_output.get())
                        list_translated.append(translated_text.text)
                        print(list_translated)
                    except:
                        pass
                
                for x, b in enumerate(boxes.splitlines()):
                    if x != 0:
                        b = b.split()
                        if len(b) == 12:
                            print(b)
                            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                            cv2.rectangle(image, (x,y), (x+w,y+h), (242,244,243), -1)
                            if b[5] == "1":
                                x1, y1, w1, h1 = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                                font = ImageFont.truetype("arial.ttf", 20)
                                img_pil = Image.fromarray(image)
                                draw = ImageDraw.Draw(img_pil)
                                draw.text((x1, y1-h1),  list_translated[q], font = font, fill = (0,0,0))
                                image = np.array(img_pil)
                                q=q+1
                cv2.imshow("Result", image)
                cv2.waitKey(0)
            except:
                pass

        #Bấm "q" để tắt camera
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera.release()
            cv2.destroyAllWindows()
            break

def convert():
    a = choose_lang_input.get()
    b = choose_lang_output.get()
    for i in range(len(value)):
        if value[i]==b:
            choose_lang_input.current(i)
        if value[i]==a:
            choose_lang_output.current(i)
    text_input.delete(1.0,'end')
    text_input.insert('end', text_output.get('1.0','end-1c'))
    text_output.delete(1.0,'end')
    translates()


lang_input = StringVar()
lang_output = StringVar()

choose_lang_input = AutocompleteCombobox(main_frame, width=20, font=("Times 10"), completevalues=list(googletrans.LANGUAGES.values()))
choose_lang_input.place(x=5, y=75)
choose_lang_input.current(21)

choose_lang_output = AutocompleteCombobox(main_frame, width=20, font=("Times 10"), completevalues=list(googletrans.LANGUAGES.values()))
choose_lang_output.place(x=5, y=275)
choose_lang_output.current(101)

#Nút translate
trans_btn = Button(main_frame, cursor="hand2", text="Translate", relief=RAISED, borderwidth=2, width=15, font=("Times 10 bold"), bg="pink", fg="white", command=translates)
trans_btn.place(x=40, y=470)
#Nút xoá
clear_btn = Button(main_frame, cursor="hand2", text="Clear", relief=RAISED, borderwidth=2, width=15, font=("Times 10 bold"), bg="pink", fg="white", command=clear)
clear_btn.place(x=250, y=470)
#Nút loa input
load_loa_image = ImageTk.PhotoImage(Image.open("iconloa.png"))
loa_input_btn = Button(main_frame, cursor="hand2", image=load_loa_image, borderwidth=0, bg="pink", command=speak_in)
loa_input_btn.place(x=369, y=230)
#Nút loa output
loa_output_btn = Button(main_frame, cursor="hand2", image=load_loa_image, borderwidth=0, bg="pink", command=speak_out)
loa_output_btn.place(x=369, y=430)
#Nút mic nhập giọng nói
load_mic_image = ImageTk.PhotoImage(Image.open("iconmic.jpg"))
mic_btn = Button(main_frame, cursor="hand2", image=load_mic_image, borderwidth=0, bg="pink", command=mic_in)
mic_btn.place(x=330, y=230)
#Nút chuyển hình ảnh thành văn bản
load_image_icon = ImageTk.PhotoImage(Image.open("iconpicture.png"))
imgtotext_btn = Button(main_frame, cursor="hand2", image=load_image_icon, borderwidth=0, bg="pink", command=openfile)
imgtotext_btn.place(x=180,y=530)
#Nút chuyển Audio thành văn bản
load_audio_icon = ImageTk.PhotoImage(Image.open("iconmuzic.png"))
audiototext_btn = Button(main_frame, cursor="hand2", image=load_audio_icon, borderwidth=0, bg="pink", command=radio_to_text)
audiototext_btn.place(x=240,y=530)
#Nút sử dụng camera
load_camera_icon = ImageTk.PhotoImage(Image.open("iconcamera.png"))
camera_btn = Button(main_frame, cursor="hand2", image=load_camera_icon, borderwidth=0, bg="pink", command=camera_realtime)
camera_btn.place(x=120,y=530)
#Nút chuyển đổi ngôn ngữ
load_convert_icon = ImageTk.PhotoImage(Image.open("iconconvert.png"))
convert_btn = Button(main_frame, cursor="hand2", image=load_convert_icon, borderwidth=0, bg="pink", command=convert)
convert_btn.place(x=190,y=262)

root.mainloop()