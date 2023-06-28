import tkinter as tk
import pymysql
from tkinter import ttk
from tkinter import messagebox



# connections

# def connection():
#     conn = pymysql.connect(
#         host = "localhost", user="root",password="",db="student_db"
#     )
#     return conn

def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",db="student_db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if lens(rows)!=0:
        stud_table.delete(*stud_table.get_children())
        for row in rows:
            stud_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()
        
        
        
        
app = tk.Tk()
app.geometry("1300x680")
app.title("SSIS version 2.0")




# functions

# placeholders for entries
# __init__ variables
id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
course =tk.StringVar()
searchin = tk.StringVar()

# placeholder values
def setph(word,num):
    if num == 1:
        id.set(word)
    if num == 1:
        name.set(word)
    if num == 1:
        sex.set(word)
    if num == 1:
        year.set(word)
    if num == 1:
        course.set(word)
    if num == 1:
        searchin.set(word)
        
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    id = str(id_entry.get())
    name = str(name_entry.get())
    sex = str(sex_entry.get())
    course = str(course_entry.get())
    year = str(year_entry.get())
    if (id =="" or id==" ") or (name =="" or name ==" ") or (sex =="" or sex ==" ") or (course =="" or course ==" ") or (year =="" or year ==" "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO student VALUES ('"+ id+"','"+name+"','"+sex+"','"+course+"','"+year+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","ID already exist")
            return
        
    fetch_data()


def reset():
    decision = messagebox.askquestion("Warning!", "Delete all data?")
    if decision != "yes":
         return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Sorry an error occured")
            return
    fetch_data()
        
def delete():
    decision = messagebox.askquestion("Warning!", "Delete the selected data?")
    if decision != "yes":
        return
    else:
        selected_item=stud_table.selection()[0]
        deleteData = str(stud_table.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE ID='"+ str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Sorry an error occured")
            return
    fetch_data()
        
def select():
    try:
        selected_item=stud_table.selection()[0]
        id = str(stud_table.item(selected_item)['values'][0])
        name = str(stud_table.item(selected_item)['values'][1])
        sex = str(stud_table.item(selected_item)['values'][2])
        year = str(stud_table.item(selected_item)['values'][3])
        course = str(stud_table.item(selected_item)['values'][4])
        setph(id,1)
        setph(name,2)
        setph(sex,3)
        setph(year,4)
        setph(course,5)
        
    except:
        messagebox.showinfo("Error","Please select a data row")
        
        
def update():
    selectedID = ""
    try:
        selected_item=stud_table.selection()[0]
        selectedID = str(stud_table.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error","Please select a data row")
    id = str(id_entry.get())
    name = str(name_entry.get())
    sex = str(sex_entry.get())
    course = str(course_entry.get())
    year = str(year_entry.get())
    if (id =="" or id==" ") or (name =="" or name ==" ") or (sex =="" or sex ==" ") or (course =="" or course ==" ") or (year =="" or year ==" "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE student SET ID='"+
                           id+"', NAME='"+
                           name+"', SEX='"+
                           sex+"', COURSE='"+
                           course+"', YEAR='"+
                           year+"', WHERE ID='"+
                           selectedID+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","ID already exist")
            return
        
    fetch_data()
    
    
        
def search():
    id = str(id_entry.get())
    name = str(name_entry.get())
    sex = str(sex_entry.get())
    course = str(course_entry.get())
    year = str(year_entry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE ID='"+
                   id+"' or NAME='"+
                   name+"' or SEX='"+
                   sex+"' or COURSE='"+
                   course+"' or YEAR='"+
                   year+"'  ")
    try:
        result = cursor.fetchall()
        for num in range (0,5):
            setph(result[0][num],(num+1))
            
        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error","No data found")
    

# Graphical User Interface

title_label = tk.Label(app, text="Simple Student Information System v2.0", font=("Arial", 30, "bold"), border=12, relief= tk.GROOVE, bg = "lightgrey")
title_label.pack(side=tk.TOP,fill=tk.X)

# frames
detail_frame = tk.LabelFrame(app, text="Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
detail_frame.place(x=20,y=90,width=450,height=575)

data_frame = tk.Frame(app, bg="lightgrey",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)




# entries and labels >> detail frame
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




# button frame
btn_frame= tk.Frame(detail_frame, bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=40,y=390,width=342,height=120)

# buttons >> btn frame
add_btn = tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15, command= add)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update",bd=7,font=("Arial",13),width=15,command= update)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15,command = delete )
delete_btn.grid(row=1,column=0,padx=2,pady=2)

select_btn = tk.Button(btn_frame, bg="lightgrey", text="Select",bd=7,font=("Arial",13),width=15, command=select)
select_btn.grid(row=1,column=1,padx=3,pady=2)



# top right frame
search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

# search and show buttons
search_label=tk.Label(search_frame,text="Search",bg="lightgrey",font=("Arial",14))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in =ttk.Combobox(search_frame,font=("Arial", 14),state="readonly",textvariable=searchin)
search_in['value']=("ID no.","Name", "Sex","Course", "Year Level")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=12,bg="lightgrey",command = search)
search_btn.grid(row=0,column=2,padx=35,pady=2)

reset_btn = tk.Button(search_frame,text="Reset",font=("Arial",13),bd=9,width=12,bg="lightgrey", command=reset)
reset_btn.grid(row=0,column=3,padx=35,pady=2)


# frame for treeview
main_frame=tk.Frame(data_frame,bg="lightgrey", bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient = tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient = tk.HORIZONTAL)


# Treeview
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


# stud_table.bind("<ButtonRelease-1>",getcur)

fetch_data()

app.mainloop()
