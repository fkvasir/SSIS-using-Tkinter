import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import messagebox

app = tk.Tk()
app.geometry("720x720")
app.title("SSIS version 2")

title_label = tk.Label(app, text="Simple Student Information System", font=("Arial", 30, "bold"), border=12, relief= tk.GROOVE, bg = "lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(app, text="Enter Details",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame = tk.Frame(app, bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)


id_label = tk.Label(detail_frame, text="ID no.",font=("Arial", 17), bg= "lightgrey")
id_label.grid(row=0,column=0,padx=2,pady=2)

id_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17))
id_entry.grid(row=0,column=1,padx=2,pady=2)

name_label = tk.Label(detail_frame, text="Name",font=("Arial", 17), bg= "lightgrey")
name_label.grid(row=1,column=0,padx=2,pady=2)

name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17))
name_entry.grid(row=1 ,column=1,padx=2,pady=2)

gender_label = tk.Label(detail_frame, text="Gender",font=("Arial", 17), bg= "lightgrey")
gender_label.grid(row=2,column=0,padx=2,pady=2)

gender_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17))
gender_entry.grid(row=2,column=1,padx=2,pady=2)

year_label = tk.Label(detail_frame, text="Year Level",font=("Arial", 17), bg= "lightgrey")
year_label.grid(row=3,column=0,padx=2,pady=2)

year_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17))
year_entry.grid(row=3,column=1,padx=2,pady=2)

course_label = tk.Label(detail_frame,text="Course", font=("Arial",17), bg="lightgrey")
course_label.grid(row=4,column=0,padx=2,pady=2)

course_box= ttk.Combobox(detail_frame, )







app.mainloop
