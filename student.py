from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Student Details")

        # =================variable===========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First img
        img1 = Image.open("college_images/face_det.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=500, height=130)

        # second img

        img2 = Image.open("college_images/vcet.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=500, y=0, width=500, height=130)
        # Third img
        img3 = Image.open("college_images/face-recognition.png")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimg3)
        first_label.place(x=1000, y=0, width=500, height=130)

        # Bg img
        img4 = Image.open(
            "college_images/pngtree-abstract-technology-background-technical-electric-image_443494.jpg")
        img4 = img4.resize((1500, 790), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_label = Label(self.root, image=self.photoimg4)
        bg_label.place(x=0, y=130, width=1500, height=790)

        # title

        label_title = Label(bg_label, text="STUDENTS DETAIlS", font=("times new roman", 35, "bold"),
                            bg="white", fg="black")
        label_title.place(x=0, y=0, width=1530, height=45)

        # main Frame

        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=5, y=55
                         , width=1470, height=690)

        # left_label_frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Info",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=640)

        img_left = Image.open("/Users/apple/Downloads/college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=5, y=0, width=690, height=130)

        # current course
        Curernt_Course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Course info",
                                          font=("times new roman", 12, "bold"))
        Curernt_Course_frame.place(x=5, y=140, width=690, height=143)

        # Department
        dep_label = Label(Curernt_Course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=15)

        dep_combo = ttk.Combobox(Curernt_Course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=25, state="readonly")
        dep_combo['values'] = ("Select Department", "CS", "IT", "Civil", "Mech", "CSE-DS", "EXTC")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        Course_label = Label(Curernt_Course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white",
                             width="20")
        Course_label.grid(row=0, column=2, padx=10)

        Course_combo = ttk.Combobox(Curernt_Course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), width=25, state="readonly")
        Course_combo['values'] = ("Select Course", "FE", "SE", "TE", "BE")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=2, pady=10)

        # YEAR
        Year_label = Label(Curernt_Course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white",
                           width="20")
        Year_label.grid(row=1, column=0, padx=10, sticky=W)

        Year_combo = ttk.Combobox(Curernt_Course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=25, state="readonly")
        Year_combo['values'] = ("Select Year", "2021-22", "2022-2023", "2023-2024", "2024-25")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_label = Label(Curernt_Course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white",
                               width=25)
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(Curernt_Course_frame, textvariable=self.var_semester,
                                      font=("times new roman", 12, "bold"), width=25, state="readonly")
        Semester_combo['values'] = ("Select Semester", "Even-Semester", "Odd-Semeter")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student infromation course
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=280, width=690, height=333)

        # Student ID
        Student_Id_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"),
                                 bg="white",
                                 width=25)
        Student_Id_label.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20,
                                    font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name

        Student_name_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"),
                                   bg="white", width=25)
        Student_name_label.grid(row=0, column=2, padx=0, pady=5, sticky=W)
        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20,
                                      font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Student Div

        Class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"),
                                bg="white", width=25)
        Class_div_label.grid(row=1, column=0, padx=0, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,
                                       font=("times new roman", 12, "bold"), width=18, state="readonly")
        class_div_combo['values'] = ("A", "B", "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No

        ROll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                              bg="white", width=25)
        ROll_no_label.grid(row=1, column=2, padx=0, pady=5, sticky=W)
        ROll_no_entry = ttk.Entry(class_student_frame, width=18, textvariable=self.var_roll,
                                  font=("times new roman", 12, "bold"))
        ROll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # gender

        Gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"),
                             bg="white", width=25)
        Gender_label.grid(row=2, column=0, padx=0, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=18
                                    , state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB

        DOB_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"),
                          bg="white", width=25)
        DOB_label.grid(row=2, column=2, padx=0, pady=5, sticky=W)
        DOB_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_dob,
                              font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        Email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"),
                            bg="white", width=25)
        Email_label.grid(row=3, column=0, padx=0, pady=5, sticky=W)
        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone NO.

        Phone_no_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"),
                               bg="white", width=25)
        Phone_no_label.grid(row=3, column=2, padx=0, pady=5, sticky=W)
        Phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,
                                   font=("times new roman", 12, "bold"))
        Phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address:

        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"),
                              bg="white", width=25)
        address_label.grid(row=4, column=0, padx=0, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,
                                  font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name:

        Teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"),
                              bg="white", width=25)
        Teacher_label.grid(row=4, column=2, padx=0, pady=5, sticky=W)
        Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20,
                                  font=("times new roman", 12, "bold"))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="take Photo sample",
                                       value="Yes")
        radiobutton1.grid(row=5, column=0)

        radiobutton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo sample",
                                       value="NO")
        radiobutton2.grid(row=5, column=1)

        # Buttons frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=685, height=48)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"),
                          bg="white", fg="black", width=23, height=2)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", font=("times new roman", 12, "bold"),
                            bg="white", fg="black", width=23, height=2, )
        update_btn.grid(row=0, column=1)

        Delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"),
                            bg="blue", fg="black", width=23, height=2)
        Delete_btn.grid(row=0, column=2)

        Reset_btn = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 12, "bold"), bg="blue",
                           fg="black", width=21, height=2)
        Reset_btn.grid(row=0, column=3)

        btn1_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=0, y=270, width=685, height=44)

        take_photo_btn = Button(btn1_frame, text="Take photo sample", command=self.generate_dataset,
                                font=("times new roman", 12, "bold"), bg="blue", fg="black", width=51, height=2)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn1_frame, height=2, command=self.generate_dataset,text="Update photo sample",
                                  font=("times new roman", 12, "bold"), bg="blue", fg="black", width=51)
        update_photo_btn.grid(row=1, column=1)

        # Right_label_frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Info",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=720, y=10, width=700, height=640)

        img_Right = Image.open("/Users/apple/Downloads/college_images/gettyimages-1022573162.jpg")
        img_Right = img_Right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        first_label = Label(Right_frame, image=self.photoimg_Right)
        first_label.place(x=5, y=0, width=690, height=130)

        # search system
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=140, width=690, height=75)

        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"),
                             bg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Semester_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=25, state="readonly")
        Semester_combo['values'] = ("Select ", "Roll_No", "Phone-No")
        Semester_combo.current(0)
        Semester_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="black",
                            width=15, height=2, padx=4)
        search_btn.grid(row=0, column=3)

        Showall_btn = Button(Search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="black",
                             width=15, height=2, padx=4)
        Showall_btn.grid(row=0, column=4)

        # ==============Table frame============
        Table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                 font=("times new roman", 12, "bold"))
        Table_frame.place(x=5, y=215, width=690, height=350)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_frame, columns=(
        "dep", "course", "year", "sem", "id", "name", "roll", "div", "gender", "dob", "email", "phone", "address",
        "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")

        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ==========function declaration=============

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error,All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="sahil1015",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Students details has been added SuccesFully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Eroor", f"Due to :{str(es)}", parent=self.root)

    # ==fetch data into table===
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="sahil1015",
                                       database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ======get-cursor======\
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error,All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="sahil1015",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update Student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))

                else:
                    if not Update:
                        return
                messagebox.showinfo('Success', 'Students Details Succesfully Updated', parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showinfo("Error", f"The Error is {str(es)}", parent=self.root)

    # =====Delete Function==========
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="sahil1015",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from Student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Succesfully Deleted Student Details", parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error", f"The Error is {str(es)}", parent=self.root)

    def reset(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set("data[5]"),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ==Generate Data Set And Take A Photo Sample======

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error,All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="sahil1015",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from Student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update Student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1
                    ))
            except Exception as es:
                messagebox.showinfo("Error", f"The Error is {str(es)}", parent=self.root)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            # ===========load predefine data on frontal face===

            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                # scaling factor=1.3
                # Minimum Neighbor=5

                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (600, 600))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Result", "Generating data set completed!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
