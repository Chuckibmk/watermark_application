from tkinter import *
from tkinter import filedialog

from PIL import Image
import matplotlib.pyplot as plt

from PIL import ImageFont
from PIL import ImageDraw

import subprocess

# Variables used for the watermarking
filep = ''
image = ''
watermark_image = ''
draw = ''
x,y = '',''
font = ''
Watertext = ''
titled = 'Text Watermark'

# this select the 1st file from file manager and saves it to filep
def selectfile():
    # ask user to select an image file
    global filep    
    filep = filedialog.askopenfilename()

    imgnm.config(text=filep)

# this inputs the watermark text
def watertxt():
    global Watertext
    Watertext = wmtxt.get()
    wmtx.configure(text='Watermark: '+Watertext)

# this selects the location of the watermark image on the main image 
def selectlcxn():    
    global x , y
    global font

    global image
    global watermark_image
    global draw

    # select text from form entry
    loc = txtloc.get()

    # creates an object of the image opened
    image = Image.open(filep)

    # creates a copy of the image, so we dont work on the original
    watermark_image = image.copy()

    # create a draw object of the image for drawing on
    draw = ImageDraw.Draw(watermark_image)

    # this gets the size of the image from the object image
    w, h = image.size
    # this if else is to sort thru the options and select the appropriate calculation
    if loc == '1':
        slwml.configure(text='Watermark Location: Top Right')
        x, y = int(w * (3/5)), int(h * (1/5))
    elif loc == '2':
        slwml.configure(text='Watermark Location: Top Left')
        x, y = int(w * (1/5)), int(h * (1/5))
    elif loc == '3':
        slwml.configure(text='Watermark Location: Down Right')
        x, y = int(w * (3/5)), int(h * (4/5))
    elif loc == '4':
        slwml.configure(text='Watermark Location: Down Left')
        x, y = int(w * (1/5)), int(h * (4/5))
    elif loc == '5':
        slwml.configure(text='Watermark Location: Middle')
        x, y = int(w / 2), int(h / 2)    
    else:
        slwml.configure(text='Select Appropriate Watermark location:\n 1 for Top Right,\n 2 for Top Left,\n 3 for Down Right,\n 4 for Down Left\n and 5 for Middle')          
    
# this selects the font size and font of the watermark text
def selectfont():
    global font
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else: 
        font_size = x

    # get text from form entry
    ttsz = txtsiz.get()

    # this if else is to sort thru the options and select the appropriate calculation
    if ttsz == '1':
        wmsiz.configure(text='Watermark Size: Large')
        font = ImageFont.truetype("arial.ttf", int(font_size/2))
    elif ttsz == '2':
        wmsiz.configure(text='Watermark Size: Medium')
        font = ImageFont.truetype("arial.ttf", int(font_size/4))
    elif ttsz == '3':
        wmsiz.configure(text='Watermark Size: Small')
        font = ImageFont.truetype("arial.ttf", int(font_size/6))
    else:
        wmsiz.configure(text='Select Appropriate Watermark Size:\n 1 for Large, \n 2 for Medium, \n 3 for Small')

# this processes the watermarking and gives you an output
def watermark():
    global titled
    draw.text((x,y), Watertext, fill=(0,0,0), font = font, anchor='ms')
    
    plt.title(titled)
    plt.imshow(watermark_image)
    plt.axis('off')
      
    plt.show()   

def close_and_open():
    # Close the current window
    root.destroy()
    # Open another Python script in a new window
    subprocess.Popen(["python", "image_watermark.py"])

# use gui to run the application,
# 1: there should be a selection for either txt or img watermark
# 2: the txt watermark should have variables for the image, txt, position of the watermark & size of the watermark
# 3: same with the image watermark

root = Tk()

root.title('Text Watermark Application')
root.geometry('500x600')

# Select watermark section
heading = Label(root, text="Select Another Watermark Type:")
heading.grid(column=0,row=0)

# select txt btn
txtbtn = Button(root, text = "Image", fg = "blue", command=close_and_open)
# select txt btn grid
txtbtn.grid(column=1,row=0)


# txt watermark section

# select image
sltxtimg = Button(root, text = "Select image:", fg = "orange", command=selectfile)
sltxtimg.grid(column=0,row=1)
# show image name

imgnm = Label(root, text="")
imgnm.grid(column=1,row=1)

# show wm text
wmtx = Label(root, text="Write Watermark: ")
wmtx.grid(column=0,row=2)

# watermark text input
wmtxt = Entry(root, width=20)
wmtxt.grid(column=1,row=2)

wmbtn = Button(root,text = "submit", fg = "red", command=watertxt)
wmbtn.grid(column=2,row=2)

# select watermark location
slwml = Label(root, text="Select Watermark location:\n 1 for Top Right,\n 2 for Top Left,\n 3 for Down Right,\n 4 for Down Left\n and 5 for Middle")
slwml.grid(column=0,row=3)

txtloc = Entry(root, width=4)
txtloc.grid(column=1,row=3)

locbtn = Button(root,text = "submit", fg = "red", command=selectlcxn)
locbtn.grid(column=2,row=3)


# select watermark size
wmsiz = Label(root, text="Select Watermark Size:\n 1 for Large, \n 2 for Medium, \n 3 for Small")
wmsiz.grid(column=0,row=4)

txtsiz = Entry(root, width=4)
txtsiz.grid(column=1,row=4)

sizbtn = Button(root,text = "submit", fg = "red", command=selectfont)
sizbtn.grid(column=2,row=4)



submit = Button(root, text = "Submit", fg = "green",command=watermark)
submit.grid(column=1,row=5)


root.mainloop()