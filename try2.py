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

id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
search=tk.StringVar()

id_label = tk.Label(detail_frame, text="ID no.",font=("Arial", 17), bg= "lightgrey")
id_label.grid(row=0,column=0,padx=2,pady=2)

id_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=id)
id_entry.grid(row=0,column=1,padx=2,pady=2)

name_label = tk.Label(detail_frame, text="Name",font=("Arial", 17), bg= "lightgrey")
name_label.grid(row=1,column=0,padx=2,pady=2)

name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=name)
name_entry.grid(row=1 ,column=1,padx=2,pady=2)

sex_label = tk.Label(detail_frame, text="Sex",font=("Arial", 17), bg= "lightgrey")
sex_label.grid(row=2,column=0,padx=2,pady=2)

sex_entry = ttk.Combobox(detail_frame,font=("Arial",15),textvariable=sex)
sex_entry['values']=("Male","Female")
sex_entry.grid(row=2,column=1,padx=2,pady=2)

year_label = tk.Label(detail_frame, text="Year Level",font=("Arial", 17), bg= "lightgrey")
year_label.grid(row=3,column=0,padx=2,pady=2)

year_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=year)
year_entry.grid(row=3,column=1,padx=2,pady=2)

course_label = tk.Label(detail_frame,text="Course", font=("Arial",17), bg="lightgrey")
course_label.grid(row=4,column=0,padx=2,pady=2)





btn_frame= tk.Frame(detail_frame, bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=22,y=390,width=342,height=120)

add_btn = tk.Button(btn_frame,bg="lightgrey",text="ADD",bd=7,font=("Arial",13),width=15)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="UPDATE",bd=7,font=("Arial",13),width=15)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey",text="ADD",bd=7,font=("Arial",13),width=15)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="UPDATE",bd=7,font=("Arial",13),width=15)
clear_btn.grid(row=1,column=1,padx=3,pady=2)

search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_label=tk.Label(search_frame,text="Search",bg="lightgrey",font=("Arial",14))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in =ttk.Combobox(search_frame,font=("Arial", 14),state="readonly",textvariable=search)
search_in['value']=("ID no.","Name", "Sex", "Year Level", "Course")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=14,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=15,pady=2)

show_btn = tk.Button(search_frame,text="Show",font=("Arial",13),bd=9,width=14,bg="lightgrey")
show_btn.grid(row=0,column=3,padx=15,pady=2)



main_frame=tk.Frame(data_frame,bg="lightgrey", bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient = tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient = tk.HORIZONTAL)

stud_table = ttk.Treeview(main_frame,columns=("ID no.","Name", "Sex","Year Level","Course"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.config(command=stud_table.yview)
x_scroll.config(command=stud_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

stud_table.column("ID no.",width=100)
stud_table.column("Name",width=100)
stud_table.column("Sex",width=100)
stud_table.column("Year Level",width=100)
stud_table.pack(fill=tk.BOTH,expand=True)
stud_table['show'] = 'headings'





app.mainloop
