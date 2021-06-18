from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import os

PATH = os.path.join("C://Users//<USERNAME>//Downloads")

# ------------------------PROCESS -----------------------#


def gen_watermark():
    file = input_1.get()
    with Image.open(f"{PATH}/{file}").convert("RGBA") as im:
        txt = Image.new('RGBA', im.size, (255, 255, 255, 0))
        fnt = ImageFont.truetype("arial.ttf", 88)
        d = ImageDraw.Draw(txt)
        heart = "\u2665"
        d.text((10 , 20), f"Made with {heart} by Shantheri", font=fnt, encoding='unic')
        out = Image.alpha_composite(im, txt)
        out.show()

# -------------------------UI Setup------------------------#


window = Tk()
window.title("Water mark manager.")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

label_x1 = Label(text="Enter image file with ext", font=("Arial", 18, "bold"))
label_x1.grid(row=0, column=0)

input_1 = Entry(width=31)
input_1.grid(row=0, column=1)

button_2 = Button(text="Generate Water Mark", width=32,font=("Arial", 8, "bold"), command=gen_watermark)
button_2.grid(row=0,column=2)


label_x2 = Label(text="By default it will look for the image in the Downloads", font=("Arial", 10, "bold"))
label_x2.grid(row=1, column=2)

window.mainloop()