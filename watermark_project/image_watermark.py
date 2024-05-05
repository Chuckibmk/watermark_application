from tkinter import *
from tkinter import filedialog
from PIL import Image
import matplotlib.pyplot as plt
import subprocess

# Variables used for the watermarking
filep = ''
filep1 = ''
image = ''
image2 = ''
crop_image = ''
x,y = '',''
a,b = '',''
titled = 'Image Watermark'

# this select the 1st file from file manager and saves it to filep
def selectfile():
    # select an image file
    global filep    
    filep = filedialog.askopenfilename()

    imgnm.config(text=filep)

# this select the 2nd file from file manager and saves it to filep1
def selectfile1():
    # select an image file
    global filep1    
    filep1 = filedialog.askopenfilename()

    imgnm1.config(text=filep1)

# this selects the location of the watermark image on the main image 
def selectlcxn():    
    global x , y 
    global image
    global image2

    # select text from form entry
    loc = txtloc.get()

    # creates an object of the image opened
    image = Image.open(filep)
    image2 = Image.open(filep1)    

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
   
# this selects the size of the watermark image
def selectsiz():    
    global a, b 
    global image
    global image2

    # select text from form entry
    txsz = txtsiz.get()  

    # this gets the size of the image from the object image
    w, h = image.size
    # this if else is to sort thru the options and select the appropriate calculation
    if txsz == '1':
        wmsiz.configure(text='Watermark Size: Large')
        a, b = int(w * (1/2)), int(h * (1/2))
    elif txsz == '2':
        wmsiz.configure(text='Watermark Size: Medium')
        a, b = int(w * (1/3)), int(h * (1/3))
    elif txsz == '3':
        wmsiz.configure(text='Watermark Size: Small')
        a, b = int(w * (1/4)), int(h * (1/4))   
    else:
        wmsiz.configure(text='Select Appropriate Watermark Size:\n 1 for Large, \n 2 for Medium, \n 3 for Small')        

# this processes the watermarking and gives you an output
def watermark():
    global crop_image
    global image
    global image2
    global x,y
    global a,b
    global titled

    # image watermark
    # size = (500,500)
    size = (a,b)
    crop_image = image2.copy()
    crop_image.thumbnail(size)

    # add watermark
    copied_image = image.copy()        
    copied_image.paste(crop_image, (x,y))

    plt.title(titled)
    plt.imshow(copied_image)
    plt.show()  

# this closes the gui window and opens another one, more like closing a page for another page
def close_and_open():
    
    root.destroy()
    # Open file in a new window
    subprocess.Popen(["python", "text_watermark.py"])


root = Tk()

root.title('Image Watermark Application')
root.geometry('500x600')

# Select watermark section
heading = Label(root, text="Select Another Watermark Type:")
heading.grid(column=0,row=0)

# select txt btn
txtbtn = Button(root, text = 'Text', fg = "blue", command=close_and_open)
# select txt btn grid
txtbtn.grid(column=1,row=0)

# select image
sltxtimg = Button(root, text = "Select image:", fg = "orange", command=selectfile)
sltxtimg.grid(column=0,row=1)

# show image name
imgnm = Label(root, text="")
imgnm.grid(column=1,row=1)

# select watermark image
sltxtimg1 = Button(root, text = "Select Watermark:", fg = "orange", command=selectfile1)
sltxtimg1.grid(column=0,row=2)

# show image name
imgnm1 = Label(root, text="")
imgnm1.grid(column=1,row=2)


# select watermark location
slwml = Label(root, text="Select Watermark location:\n 1 for Top Right,\n 2 for Top Left,\n 3 for Down Right,\n 4 for Down Left\n and 5 for Middle")
slwml.grid(column=0,row=3)

# location entry form
txtloc = Entry(root, width=4)
txtloc.grid(column=1,row=3)

# location entry butn
locbtn = Button(root,text = "submit", fg = "red", command=selectlcxn)
locbtn.grid(column=2,row=3)


# select watermark size
wmsiz = Label(root, text="Select Watermark Size:\n 1 for Large, \n 2 for Medium, \n 3 for Small")
wmsiz.grid(column=0,row=4)

# size entry form
txtsiz = Entry(root, width=4)
txtsiz.grid(column=1,row=4)

# size entry btn
sizbtn = Button(root,text = "submit", fg = "red", command=selectsiz)
sizbtn.grid(column=2,row=4)

#run the watermark 
submit = Button(root, text = "Submit", fg = "green",command=watermark)
submit.grid(column=1,row=5)

root.mainloop()