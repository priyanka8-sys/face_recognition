from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from tkinter import filedialog
import shutil
import csv


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recognition System")

        # ==================== Variables ==================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dept = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()
        self.mydata = []

        # ================== Header Images ==================
        try:
            img = Image.open(r"college_images\s1.jpg")
            img = img.resize((950, 200), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=950, height=200)

            img1 = Image.open(r"college_images\s2.jpg")
            img1 = img1.resize((950, 200), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl = Label(self.root, image=self.photoimg1)
            f_lbl.place(x=950, y=0, width=950, height=200)

            # Background Image
            img4 = Image.open(r"college_images\j.jpg")
            img4 = img4.resize((1920, 1070), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            bg_img = Label(self.root, image=self.photoimg4)
            bg_img.place(x=0, y=200, width=1920, height=1070)
        
        except FileNotFoundError:
            # Handle the case where images are not found
            messagebox.showerror("Error", "Image files not found. Please check the file paths.", parent=self.root)
            bg_img = Label(self.root, bg="lightgrey")
            bg_img.place(x=0, y=200, width=1920, height=1070)

        # Main Title
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=55, width=1860, height=1100)

        # ================== Left Label Frame ==================
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=20, y=10, width=900, height=800)

        try:
            img_left = Image.open(r"college_images\face.jpg")
            img_left = img_left.resize((850, 200), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl = Label(Left_Frame, image=self.photoimg_left)
            f_lbl.place(x=15, y=0, width=870, height=200)
        except FileNotFoundError:
            f_lbl = Label(Left_Frame, text="[Image Placeholder]", bg="lightblue", font=("times new roman", 12))
            f_lbl.place(x=15, y=0, width=870, height=200)

        # Frame for student details labels and entries
        Frame_left = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE)
        Frame_left.place(x=10, y=200, width=870, height=300)

        # Labels and Entries for student details
        # Attendance ID
        attendence_id_label = Label(Frame_left, text="Attendance ID:", font=("times new roman", 17, "bold"), bg="white")
        attendence_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendence_id_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_id, font=("times new roman", 17, "bold"))
        attendence_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(Frame_left, text="Roll No:", font=("times new roman", 17, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_roll, font=("times new roman", 17, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(Frame_left, text="Name:", font=("times new roman", 17, "bold"), bg="white")
        name_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        name_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_name, font=("times new roman", 17, "bold"))
        name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(Frame_left, text="Department:", font=("times new roman", 17, "bold"), bg="white")
        department_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        department_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_dept, font=("times new roman", 17, "bold"))
        department_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(Frame_left, text="Time:", font=("times new roman", 17, "bold"), bg="white")
        time_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        time_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_time, font=("times new roman", 17, "bold"))
        time_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(Frame_left, text="Date:", font=("times new roman", 17, "bold"), bg="white")
        date_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        date_entry = ttk.Entry(Frame_left, textvariable=self.var_atten_date, font=("times new roman", 17, "bold")) 
        date_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Attendance Status
        status_label = Label(Frame_left, text="Status:", font=("times new roman", 17, "bold"), bg="white")
        status_label.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        status_combo = ttk.Combobox(Frame_left, textvariable=self.var_atten_status, font=("times new roman", 17, "bold"), state="readonly")
        status_combo["values"] = ("Present", "Absent") 
        status_combo.grid(row=6, column=1, padx=10, pady=5, sticky=W)
        status_combo.current(0)

        # Button Frame
        button_frame = Frame(Left_Frame, bd=2, bg="white", relief=RIDGE)
        button_frame.place(x=10, y=500, width=870, height=60)

        # Import CSV button
        import_button = Button(button_frame, text="Import CSV", command=self.import_csv, width=17, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        import_button.grid(row=0, column=0, padx=1, pady=5, sticky=W)

        # Export CSV button
        export_button = Button(button_frame, text="Export CSV", command=self.export_csv, width=17, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        export_button.grid(row=0, column=1, padx=1, pady=5, sticky=W)

        # Update button
        update_button = Button(button_frame, text="Update", width=17, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        update_button.grid(row=0, column=2, padx=1, pady=5, sticky=W)

        # Reset button
        reset_button = Button(button_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        reset_button.grid(row=0, column=3, padx=1, pady=5, sticky=W)

        # ================== Right Label Frame ==================
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=930, y=10, width=900, height=750)

        table_frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=10, width=880, height=650)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, columns=("attendence_id", "roll_no", "name", "department", "time", "date", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("attendence_id", text="Attendance ID")
        self.attendance_table.heading("roll_no", text="Roll No") 
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"
        self.attendance_table.column("attendence_id", width=100)
        self.attendance_table.column("roll_no", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("department", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("status", width=100)
        
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    # ==================== Functions ====================
    def fetch_data(self):
        """Populates the Treeview with data from the global 'mydata' list."""
        self.attendance_table.delete(*self.attendance_table.get_children())
        for row in self.mydata:
            self.attendance_table.insert("", END, values=row)

    def import_csv(self):
        """Opens a file dialog to import a CSV file and loads the data into the table."""
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        if not fln:
            return
        
        self.mydata = []
        with open(fln, newline="") as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                self.mydata.append(i)
        
        self.fetch_data()
        messagebox.showinfo("Import Success", "Data imported successfully.", parent=self.root)

    def export_csv(self):
        """Saves the data from the Treeview to a CSV file."""
        try:
            if not self.mydata:
                messagebox.showerror("No Data", "No data to export.", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            if not fln.endswith(".csv"):
                fln += ".csv"
            
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in self.mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data was exported to {os.path.basename(fln)} successfully.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        """Populates the entry fields with data from the selected row in the table."""
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        rows = content['values']
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dept.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_status.set(rows[6])

    def reset_data(self):
        """Clears all data from the entry fields."""
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("Present")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()