from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
import os
from tkinter import messagebox
from time import strftime   
from datetime import datetime

from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import developer
from help import help
import tkinter



class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("face recogition system")
        #first image
        img=Image.open(r"college_images\71.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

       #2nd image
        img1=Image.open(r"college_images\71.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #3rd image
        img2=Image.open(r"college_images\71.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2) # type: ignore

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #image4
        img3=Image.open(r"college_images\71.jpg")
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


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new romen",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1920,height=45)



        #==================== time ====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl = Label(bg_img, font=("times new roman", 14, "bold"), bg="white", fg="blue")
        lbl.place(x=30, y=0, width=110, height=40)
        time()

        #stdent button
        img5=Image.open(r"college_images\student.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=200,width=220,height=220)


        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=400,width=220,height=40)


         #detect face button
        img6=Image.open(r"college_images\face detection.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_details)
        b1.place(x=700,y=200,width=220,height=220)


        b1_1=Button(bg_img,text="Face Detecter",cursor="hand2",command=self.face_details,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=400,width=220,height=40)


        #attendence face button
        img7=Image.open(r"college_images\attendence.jpg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendence_details)
        b1.place(x=1100,y=200,width=220,height=220)


        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_details,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=400,width=220,height=40)


        #helpface button
        img8=Image.open(r"college_images\help.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_details)
        b1.place(x=1500,y=200,width=220,height=220)


        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_details,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1500,y=400,width=220,height=40)
     

        #train face button
        img9=Image.open(r"college_images\train.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_details)
        b1.place(x=300,y=500,width=220,height=220)


        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_details,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=300,y=700,width=220,height=40)


         #photos  face button
        img10=Image.open(r"college_images\photos.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=700,y=500,width=220,height=220)


        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=700,y=700,width=220,height=40)


        #developer face button
        img11=Image.open(r"college_images\developer.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_details)
        b1.place(x=1100,y=500,width=220,height=220)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_details,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=700,width=220,height=40)


        #exit facebutton
        img12=Image.open(r"college_images\exit.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit_program)
        b1.place(x=1500,y=500,width=220,height=220)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_program,font=("times new romen",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1500,y=700,width=220,height=40)
      


    def open_img(self):
        os.startfile("data")

    def exit_program(self):
        self.exit_program=tkinter.messagebox.askyesno("Face Recognition System","Are you sure you want to exit?",parent=self.root)
        if self.exit_program>0:
            self.root.destroy()
        else:
            return



        #==================  function button ====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
     

    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)



    def developer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)

    def help_details(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)














if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()