import pyautogui
import tkinter as tk
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

root = tk.Tk()
root.geometry("300x200")
root.attributes("-alpha", 0.2, "-topmost", True)

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
    global path
    path = "d:/ssd/vscode/new stuff/OCRtranslator/ss.png"

    x,y,w,h = get_coordinates()
    root.withdraw()
    root.after(150,screenshot(x,y,w,h,path))
    root.after(150,root.destroy())
    

root.bind("<k>", on_k)
root.mainloop()

result = reader.readtext(path, detail=0, paragraph=True)
print(result)