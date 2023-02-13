from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os


class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        #First img
        img1=Image.open("college_images/vcet.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_label=Label(self.root,image=self.photoimg1)
        first_label.place(x=0,y=0,width=500,height=130)

        #second img

        img2 = Image.open("college_images/facialrecognition.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=500, y=0, width=500, height=130)
        #Third img
        img3 = Image.open("college_images/u.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimg3)
        first_label.place(x=1000, y=0, width=500, height=130)

        # Bg img
        img4 = Image.open("college_images/pngtree-abstract-technology-background-technical-electric-image_443494.jpg")
        img4 = img4.resize((1500, 790), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_label = Label(self.root, image=self.photoimg4)
        bg_label.place(x=0, y=130, width=1500, height=790)

        #title

        label_title=Label(bg_label,text="FACE RECONITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        label_title.place(x=0,y=0,width=1530,height=45)

        #Buttons
        #1.student Button


        img5 = Image.open("college_images/117-1176594_student-learning-education-college-student-vector-png-transparent.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)


        b1=Button(bg_label,image=self.photoimg5,command=self.student_details,cursor="hand")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_label, text="Student Details",command=self.student_details, cursor="hand",font=("times new roman",15,"bold"),bg="blue",fg="Black")
        b1_1.place(x=200, y=300, width=220, height=40)

        # 2.Detect face Button
        img6 = Image.open("college_images/facedetector.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_label, image=self.photoimg6, cursor="hand")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_label, text="Face Detector", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",
                      fg="Black")
        b1_1.place(x=500, y=300, width=220, height=40)

        # 3.Attendence Button

        img7 = Image.open(
            "college_images/attendance-icon.webp")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_label, image=self.photoimg7, cursor="hand")
        b1.place(x=800
                 , y=100, width=220, height=220)

        b1_1 = Button(bg_label, text="Attendence", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",
                      fg="Black")
        b1_1.place(x=800, y=300, width=220, height=40)

        # 4.Info Button


        img8 = Image.open(
            "college_images/help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg"
            "")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_label, image=self.photoimg8, cursor="hand")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_label, text="INFO", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",
                      fg="Black")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # 5.Train data Button

        img9 = Image.open(
            "college_images/Train.jpg"
            "")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_label, image=self.photoimg9, cursor="hand")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_label, text="Train Data", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",fg="Black")
        b1_1.place(x=200, y=580, width=220, height=40)

        # 6.Photos train Button

        img10 = Image.open(
            "college_images/opencv_face_reco_more_data.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_label, image=self.photoimg10, cursor="hand",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_label, text="Photos", cursor="hand",command=self.open_img, font=("times new roman", 15, "bold"), bg="blue",
                      fg="Black")
        b1_1.place(x=500, y=580, width=220, height=40)

        # 7.Devlopers Button

        img11 = Image.open(
            "college_images/dec.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_label, image=self.photoimg11, cursor="hand")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_label, text="Devlopers", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",
                      fg="Black")
        b1_1.place(x=800, y=580, width=220, height=40)

        # 8.Exit Button

        img12 = Image.open("college_images/Exit.jpg")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_label, image=self.photoimg12, cursor="hand")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_label, text="Exit", cursor="hand", font=("times new roman", 15, "bold"), bg="blue",fg="Black")
        b1_1.place(x=1100, y=580, width=220, height=40)





    def open_img(self):
        os.startfile("//Users//apple//PycharmProjects//face_recognisation_attendence_system")
        # Function buttons

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)






if __name__ =="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()