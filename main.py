import pyautogui
import tkinter as tk
import easyocr
from langdetect import detect
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)
import os

txt_path = "d:/ssd/vscode/new stuff/OCRtranslator/text.txt"

#initializing the OCR object and putting which languages to detect
reader = easyocr.Reader(['en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'da', 'sv', 'pl', 'ro', 'tr'], gpu=True)

#a dictionary for languages that get detected by langdetect library and then 
#refers to the mymemorytranslator module language names
MYMEMORY_CODES = {
    "en": "en-US",
    "fr": "fr-FR",
    "es": "es-ES",
    "de": "de-DE",
    "it": "it-IT",
    "pt": "pt-PT",
    "nl": "nl-NL",
    "da": "da-DK",
    "sv": "sv-SE",
    "pl": "pl-PL",
    "ro": "ro-RO",
    "tr": "tr-TR",
}

#tkinter window attributes
root = tk.Tk()
root.geometry("300x200")
root.attributes("-alpha", 0.4, "-topmost", True)

def get_coordinates():
    #defining the function which gives the coordinates of the window
    #coordinates of the top left corner ( x )
    x = root.winfo_rootx()
    #coordinates of the top left corner ( y )
    y = root.winfo_rooty()
    #width
    width = root.winfo_width()
    #height 
    height = root.winfo_height()
    
    return x, y,width,height

def screenshot(x,y,w,h, path):
    #defining the screenshot function to take a screenshot using pyautogui
    #(x-start, y-start, width, heigh)
    region_box = (x,y,w,h)
    screenshot = pyautogui.screenshot(region=region_box)
    screenshot.save(path)


def on_k(event):
    #defining the function that works if the user presses "k"
    global png_path
    png_path = "d:/ssd/vscode/new stuff/OCRtranslator/ss.png"

    x,y,w,h = get_coordinates()
    root.withdraw()
    root.after(150,screenshot(x,y,w,h,png_path))
    root.after(150,root.destroy())
    

root.bind("<k>", on_k)
root.mainloop()

#ocr module implementation
result = reader.readtext(png_path, detail=0, paragraph=True)
with open(txt_path, "w") as f:
    f.write(str(result))

#storing the text the OCR output into a variable
with open(txt_path, "r" ) as f:
    text = f.read()

#using the langdetect module to detect languages
lang = detect(text)
srclang = MYMEMORY_CODES.get(lang, lang)

#passing the text to the translator module
translated = MyMemoryTranslator(source=srclang, target="en-US").translate(text)
with open(txt_path, "w") as f:
    f.write(str(translated))

#deleting the photo
try:
    os.remove(png_path)
    print("Removed the png file")

except "FileNotFound":
    print("File not found.")

#storing the translated text in the file to a variable and printing it
with open(txt_path, "r" ) as f:
    text = f.read()
print("=====Translated text ======")
print(text)
print("===========================")

#deleting the text file
try:
    os.remove(txt_path)
    print("Text file removed successfully")

except "FileNotFound":
    print("File not found")