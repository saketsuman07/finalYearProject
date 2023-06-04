from tkinter import  *

import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import cv2




root =Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.config(bg="white")
bg = ImageTk.PhotoImage(file="images/frnt.jpg")
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
my_canvas = Canvas(root, width=800, height=800)
my_canvas.pack(fill=BOTH, expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_text(650, 65, text="welcome, Prayukti 2023", fill="white", font=("times new roman", 70))
def oreg():
    root.destroy()
    import register
def olog():
    root.destroy()
    import login
image = Image.open("images/kp.png")
resize_image = image.resize((300, 70))
left2 = ImageTk.PhotoImage(resize_image)

#Let us create a label for button event
img_label= Label(image=left2)
#Let us create a dummy button and pass the image


button= Button(root, image=left2,command=oreg,
borderwidth=0)
button.place(x=800,y=300)

#login
image2 = Image.open("images/kpr.jpg")
resize_image2 = image2.resize((300, 70))
left3 = ImageTk.PhotoImage(resize_image2)

#Let us create a label for button event
img_label2= Label(image=left3)
#Let us create a dummy button and pass the image
button2= Button(root, image=left3,command=olog,
borderwidth=0)
button2.place(x=500,y=300)




root.mainloop()
