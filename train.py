from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Train Data")

        label_title = Label(self.root, text="TRIAN DATA SET", font=("times new roman", 35, "bold"),
                            bg="white", fg="RED")
        label_title.place(x=0, y=0, width=1530, height=45)

        img_left = Image.open("college_images/facialrecognition.png")
        img_left = img_left.resize((1500, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_left)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1530, height=325)

        img_bottom = Image.open("college_images/facialrecognition.png")
        img_bottom = img_bottom.resize((1500, 325), Image.ANTIALIAS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        first_label = Label(self.root, image=self.photoimg_bottom)
        first_label.place(x=0, y=440, width=1530, height=325)




if __name__ == "__main__":
    root = Tk()
    obj = Train\
        (root)
    root.mainloop()
