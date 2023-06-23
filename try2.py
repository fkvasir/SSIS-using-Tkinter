import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import messagebox

app = tk.Tk()
app.geometry("1080x1080")
app.title("SSIS version 2")

title_label = tk.Label(app, text="Simple Student Information System", font=("Arial", 30, "bold"), border=12, relief= tk.GROOVE, bg = "lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(app, text="Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=450,height=575)

data_frame = tk.Frame(app, bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)



id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
search=tk.StringVar()
course =tk.StringVar()



id_label = tk.Label(detail_frame, text="ID no.",font=("Arial", 13), bg= "lightgrey")
id_label.grid(row=0,column=0,padx=2,pady=2)

id_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=id)
id_entry.grid(row=0,column=1,padx=2,pady=2)

name_label = tk.Label(detail_frame, text="Name",font=("Arial", 13), bg= "lightgrey")
name_label.grid(row=1,column=0,padx=2,pady=15)

name_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=name)
name_entry.grid(row=1 ,column=1,padx=2,pady=15)

sex_label = tk.Label(detail_frame, text="Sex",font=("Arial", 13), bg= "lightgrey")
sex_label.grid(row=2,column=0,padx=2,pady=15)

sex_entry = ttk.Combobox(detail_frame,font=("Arial",16),textvariable=sex)
sex_entry['values']=("Male","Female")
sex_entry.grid(row=2,column=1,padx=2,pady=15)

course_label = tk.Label(detail_frame,text="Course", font=("Arial",13), bg="lightgrey")
course_label.grid(row=3,column=0,padx=2,pady=15)

course_entry = ttk.Combobox(detail_frame,font=("Arial",16),textvariable=course)
course_entry['values']=("Computer Science","Public Administration")
course_entry.grid(row=3,column=1,padx=2,pady=15)

year_label = tk.Label(detail_frame, text="Year Level",font=("Arial", 13), bg= "lightgrey")
year_label.grid(row=4,column=0,padx=2,pady=15)

year_entry = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=year)
year_entry.grid(row=4,column=1,padx=2,pady=15)



# FUNCTIONS
def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * from data")
    rows = curr.fetchall()
    if len(rows)!=0:
        stud_table.delete(*stud_table.get_children())
        for row in rows:
            stud_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()

def add_data():
    if id.get() == "" or name.get()=="" or sex.get()=="" or course.get()==""or year.get()=="":
        messagebox.showerror("Error!")
    else:
        conn = pymysql.connect(host="localhost",user="root", password="sms1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s)",(id.get(),name.get(),sex.get(),course.get(),year.get()))
        conn.commit()
        conn.close()

        fetch_data()


def getcur(event): #fetch data of selected row
    cursor_row = stud_table.focus()
    content = stud_table.item(cursor_row)
    row= content['values']
    id.set(row[0])
    name.set(row[1])
    sex.set(row[2])
    course.set(row[3])
    year.set(row[4])

def clear():
    id.set("")
    name.set("")
    sex.set("")
    course.set("")
    year.set("")

def update_data():
    conn = pymysql.connect(host="localhost",user="root",password="", database="sms1")
    curr = conn.cursor()
    curr.execute()
    conn.commit()
    conn.close()

    fetch_data()


btn_frame= tk.Frame(detail_frame, bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=40,y=390,width=342,height=120)

add_btn = tk.Button(btn_frame,bg="lightgrey",text="ADD",bd=7,font=("Arial",13),width=15,command=add_data)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="UPDATE",bd=7,font=("Arial",13),width=15,command=update_data)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey",text="DELETE",bd=7,font=("Arial",13),width=15)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame, bg="lightgrey", text="CLEAR",bd=7,font=("Arial",13),width=15,command=clear)
clear_btn.grid(row=1,column=1,padx=3,pady=2)




search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_label=tk.Label(search_frame,text="Search",bg="lightgrey",font=("Arial",14))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in =ttk.Combobox(search_frame,font=("Arial", 14),state="readonly",textvariable=search)
search_in['value']=("ID no.","Name", "Sex", "Year Level", "Course")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=12,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=35,pady=2)

show_btn = tk.Button(search_frame,text="Show",font=("Arial",13),bd=9,width=12,bg="lightgrey")
show_btn.grid(row=0,column=3,padx=35,pady=2)


main_frame=tk.Frame(data_frame,bg="lightgrey", bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient = tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient = tk.HORIZONTAL)

stud_table = ttk.Treeview(main_frame,columns=("ID no.","Name", "Sex","Course","Year Level"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=stud_table.yview)
x_scroll.config(command=stud_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

stud_table.heading("ID no.",text="ID no")
stud_table.heading("Name",text="Name")
stud_table.heading("Sex",text="Sex")
stud_table.heading("Course",text="Course")
stud_table.heading("Year Level",text="Year Level")

stud_table['show'] = 'headings'

stud_table.column("ID no.",width=100)
stud_table.column("Name",width=100)
stud_table.column("Sex",width=100)
stud_table.column("Course",width=100)
stud_table.column("Year Level",width=100)
stud_table.pack(fill=tk.BOTH,expand=True)


stud_table.bind("<ButtonRelease-1>",getcur)

fetch_data()

app.mainloop()

