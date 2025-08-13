from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import filedialog
import shutil

class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x1200+0+0")
        self.root.title("face recogition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1900,height=50)

        #first image
        img=Image.open(r"college_images\dev.jpg")    
        img = img.resize((1900, 1100), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=1900,height=1100)


      
       



if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()