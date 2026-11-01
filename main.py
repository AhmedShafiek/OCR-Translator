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


txt_path = "d:/ssd/vscode/new stuff/OCRtranslator/text.txt"

reader = easyocr.Reader(['en', 'fr', 'es', 'de', 'it', 'pt', 'nl', 'da', 'sv', 'pl', 'ro', 'tr'], gpu=True)

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

root = tk.Tk()
root.geometry("300x200")
root.attributes("-alpha", 0.4, "-topmost", True)

def get_coordinates():
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
    #(x-start, y-start, width, heigh)
    region_box = (x,y,w,h)
    screenshot = pyautogui.screenshot(region=region_box)
    screenshot.save(path)

def on_k(event):
    global png_path
    png_path = "d:/ssd/vscode/new stuff/OCRtranslator/ss.png"

    x,y,w,h = get_coordinates()
    root.withdraw()
    root.after(150,screenshot(x,y,w,h,png_path))
    root.after(150,root.destroy())
    

root.bind("<k>", on_k)
root.mainloop()

result = reader.readtext(png_path, detail=0, paragraph=True)
with open(txt_path, "w") as f:
    f.write(str(result))

with open(txt_path, "r" ) as f:
    text = f.read()

lang = detect(text)
srclang = MYMEMORY_CODES.get(lang, lang)

translated = MyMemoryTranslator(source=srclang, target="en-US").translate(text)
with open(txt_path, "w") as f:
    f.write(str(translated))
