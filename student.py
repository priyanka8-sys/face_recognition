from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog
import shutil

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("face recogition system")


        #===================variables=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


         #first imagee recognition\
        img=Image.open(r"college_images\s1.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

       #2nd image
        img1=Image.open(r"college_images\s2.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #3rd image
        img2=Image.open(r"college_images\s3.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2) # type: ignore

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #image4
        img3=Image.open(r"college_images\s4.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3) # type: ignore

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1500,y=0,width=500,height=130)
        
        #bg image
        img4=Image.open(r"college_images\j.jpg")
        img4 = img4.resize((1920, 1070), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4) # type: ignore

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1920,height=1070)


        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new romen",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1920,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=55,width=1860,height=1100  )



        #left label frame

        Left_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=20,y=10,width=900,height=800)
        
        img_left=Image.open(r"college_images\h.jpg")
        img_left = img_left.resize((850, 200), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) # type: ignore

        f_lbl=Label(Left_Frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=0,width=870,height=200)
       
       #current course information

        current_course_frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=18,y=200,width=870,height=150)

        #department
        dep_label=Label(current_course_frame,text="Department:",font=("times new romen",17,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new romen",17,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=15,sticky=W)


        
         #couse
        course_label=Label(current_course_frame,text="Course:",font=("times new romen",17,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new romen",17,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=15,sticky=W)


         #year
        year_label=Label(current_course_frame,text="Year:",font=("times new romen",17,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new romen",17,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
         #semester
        sem_label=Label(current_course_frame,text="Semester:",font=("times new romen",17,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)


        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new romen",17,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=18,y=350,width=870,height=410)

        #student id
        studentid_label=Label(class_student_frame,text="StudentID:",font=("times new romen",15,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)


        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new romen",15,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

         #student name
        studentname_label=Label(class_student_frame,text="Student name:",font=("times new romen",15,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)


        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new romen",15,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

         #student division
        studentdiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",15,"bold"),bg="white")
        studentdiv_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),width=20,state="readonly")
        div_combo["values"]=("A","B","C","D","E","F")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         #roll no
        studentroll_label=Label(class_student_frame,text="Roll no:",font=("times new romen",15,"bold"),bg="white")
        studentroll_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)


        studentroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new romen",15,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

         #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new romen",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new romen",15,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

         #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new romen",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)


        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new romen",15,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)


        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new romen",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)


        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new romen",15,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

         #phone no
        phone_label=Label(class_student_frame,text="Phone no:",font=("times new romen",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)


        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new romen",15,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

         #address
        address_label=Label(class_student_frame,text="Address",font=("times new romen",15,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)


        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new romen",15,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

         #teacher name
        teacher_label=Label(class_student_frame,text="Teacher name:",font=("times new romen",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)


        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new romen",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)


        #radio buttons

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="no")
        radiobtn2.grid(row=6,column=1)



         #bb buttons frame
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=10,y=280,width=850,height=40)

        save_btn=Button(button_frame,command=self.add_data,text="Save",width=17,font=("times new romen",14,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        
        update_btn=Button(button_frame,command=self.update_data,text="Update",width=17,font=("times new romen",14,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=17,font=("times new romen",14,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new romen",14,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        button_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=10,y=320,width=850,height=40)

        take_photo_btn=Button(button_frame1,command=self.generate_dataset,text="take photo sample",width=35,font=("times new romen",14,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(button_frame1,command=self.upload_photo,text="Update photo sample",width=35,font=("times new romen",14,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)




        #right label frame

        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=930,y=10,width=900,height=800)

        img_right=Image.open(r"C:\Users\avina\Desktop\projects\face recognition\college_images\student.jpg")
        img_right = img_right.resize((850, 200), Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right) # type: ignore

        f_lbl=Label(Right_Frame,image=self.photoimg_right)
        f_lbl.place(x=15,y=0,width=870,height=200)


        #=========search system=========
        search_frame=LabelFrame(Right_Frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        search_frame.place(x=18,y=200,width=870,height=90)

        search_label=Label(search_frame,text="Search by:",font=("times new romen",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new romen",17,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select ","Roll No","phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=20,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new romen",15,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=14,font=("times new romen",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showall_btn=Button(search_frame,text="Show all",width=14,font=("times new romen",11,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=3)


        #=========table frame=========
        table_frame=LabelFrame(Right_Frame,bd=5,bg="white",relief=RIDGE)
        table_frame.place(x=18,y=300,width=870,height=470)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo") ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  

    #===================function decoration=================

    def add_data(self):
        if (
            self.var_std_id.get() == "" or
            self.var_std_name.get() == "" or
            self.var_roll.get() == "" or
            self.var_dep.get() == "Select Department"
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="avinash123@#!",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
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
                    )
                )
                conn.commit()
                self.fetch_data()  
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}",parent=self.root)


    #=================== fetch data ==========
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="avinash123@#!",
            database="face_recognizer"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()   

    #===================get cursor function=========
    def get_cursor(self, event=""):
        cursor_focus= self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])   


    #==============update function=========
    def update_data(self):
        if (
            self.var_std_id.get() == "" or
            self.var_std_name.get() == "" or
            self.var_roll.get() == "" or
            self.var_dep.get() == "Select Department"
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if not update:
                return
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="avinash123@#!",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT student_id FROM student WHERE student_id=%s", (self.var_std_id.get(),))
            result = my_cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "Student ID does not exist.", parent=self.root)
                conn.close()
                return
            my_cursor.execute("""
                UPDATE student 
                SET dep=%s, course=%s, year=%s, semester=%s, name=%s, `division`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                WHERE student_id=%s
            """, (
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
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update student details. Due to: {str(e)}", parent=self.root)
    #===================delete function=========
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="avinash123@#!",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete student details. Due to: {str(e)}", parent=self.root)

    #===================reset function=========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #===================take photo sample function=========
    def generate_dataset(self):
        if (
            self.var_std_id.get() == "" or
            self.var_std_name.get() == "" or
            self.var_roll.get() == "" or
            self.var_dep.get() == "Select Department"
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="avinash123@#!",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("""
                    UPDATE student 
                    SET dep=%s, course=%s, year=%s, semester=%s, name=%s, `division`=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                    WHERE student_id=%s
                """, (
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
                    self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None  # No face detected

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        print("Failed to grab frame from camera")
                        break

                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1

                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = f"data/user.{str(id)}.{str(img_id)}.jpg"
                        cv2.imwrite(file_name_path, face)

                        # ✅ Added position (10, 50) for the text
                        cv2.putText(face, str(img_id), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)


                    # Exit if Enter key (13) pressed or 100 images collected
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate dataset. Due to: {str(e)}", parent=self.root)

    #=====================upload photo sample function=========
    def upload_photo(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="avinash123@#!",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student WHERE student_id=%s", (self.var_std_id.get(),))
                data = my_cursor.fetchone()
                if data is None:
                    messagebox.showerror("Error", "Student ID does not exist.", parent=self.root)
                    conn.close()
                    return

                file_path = filedialog.askopenfilename(
                    title="Select Photo",
                    filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
                )
                if not file_path:
                    messagebox.showwarning("Warning", "No file selected.", parent=self.root)
                    conn.close()
                    return

                dest_dir = "data"
                dest_path = f"{dest_dir}/user.{self.var_std_id.get()}.uploaded.jpg"
                shutil.copy(file_path, dest_path)

                my_cursor.execute(
                    "UPDATE student SET photosample=%s WHERE student_id=%s",
                    ("yes", self.var_std_id.get())
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Photo uploaded successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload photo. Due to: {str(e)}", parent=self.root)









































if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
    