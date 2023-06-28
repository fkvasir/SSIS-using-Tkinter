import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox




  
app = tk.Tk()
app.geometry("1300x680")
app.title("SSIS version 2.0")


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
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add(name, id_number, gender, year_level, course):
    id = str(id_entry.get())
    name = str(name_entry.get())
    sex = str(sex_entry.get())
    course = str(course_entry.get())
    year = str(year_entry.get())

    # Connect to database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    if (id =="" or id==" ") or (name =="" or name ==" ") or (sex =="" or sex ==" ") or (course =="" or course ==" ") or (year =="" or year ==" "):  # if entries are empty >>
        messagebox.showinfo("Error", "Please fill up the blank entry") # >> will show an error
        return
    else:
        try:
            cursor.execute('''INSERT INTO students (name, id_number, gender, year_level, course)
                      VALUES (?, ?, ?, ?, ?)''', (name, id_number, gender, year_level, course))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error","ID already exist")
            return


def reset_data():
    
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM students''')

    conn.commit()
    conn.close()
    messagebox.showinfo("Success","All students data reset.")


def delete():
    selected_id = id_entry.get()

    
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM students WHERE id_number = ?''', (selected_id,))
    
    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data deleted successfully.")
    else:
        messagebox.showinfo("Error", "No matching student found.")

        
def select(event):
    try:
        selected_item = stud_table.focus()
        selected_data = stud_table.item(selected_item)['values']
        if selected_data:
            id_entry.delete(0, tk.END)
            id_entry.insert(tk.END, selected_data[0])
            name_entry.delete(0, tk.END)
            name_entry.insert(tk.END, selected_data[1])
            gender_entry.delete(0, tk.END)
            gender_entry.insert(tk.END, selected_data[2])
            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, selected_data[3])
            course_entry.delete(0, tk.END)
            course_entry.insert(tk.END, selected_data[4])
        
    except:
        messagebox.showinfo("Error","Please select a data row")
        
        
def update():
    selected_id = id_entry.get()
    new_name = name_entry.get()
    new_gender = gender_entry.get()
    new_year = year_entry.get()
    new_course = course_entry.get()


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute('''UPDATE students SET name=?, gender=?, year_level=?, course=? WHERE id_number=?''',
                   (new_name, new_gender, new_year, new_course, selected_id))

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data updated successfully.")
    else:
        messagebox.showinfo("Error", "No matching student found.")

    # Clear the entry fields
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    refresh_data()

# Function to refresh the data in the tree view
def refresh_data():
    # Clear the tree view
    stud_table.delete(*stud_table.get_children())

    
    results = read()

    for result in results:
        stud_table.insert("", tk.END, values=result)
    
    
        

def search():
    search_term = searchin.get()

    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Execute the search query
    cursor.execute("SELECT * FROM students WHERE id_number LIKE ? OR name LIKE ? OR gender LIKE ? OR year_level LIKE ? OR course LIKE ?",
                   (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))

    results = cursor.fetchall()

    # Clear the tree view
    stud_table.delete(*stud_table.get_children())

    # Insert the search results into the tree view
    for result in results:
        stud_table.insert("", tk.END, values=result)

    conn.close()
    

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
add_btn = tk.Button(btn_frame,bg="lightgrey",text="Add",bd=7,font=("Arial",13),width=15, command=add)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update",bd=7,font=("Arial",13),width=15,command=update)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="lightgrey",text="Delete",bd=7,font=("Arial",13),width=15,command=delete )
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
# Create a tree view to display the student data
stud_table = ttk.Treeview(window)
stud_table["columns"] = ("ID Number", "Name", "Gender", "Year Level", "Course")
stud_table.heading("ID Number", text="ID Number")
stud_table.heading("Name", text="Name")
stud_table.heading("Gender", text="Gender")
stud_table.heading("Year Level", text="Year Level")
stud_table.heading("Course", text="Course")
stud_table.pack()

# Populate the tree view with data
results = read()
for result in results:
    stud_table.insert("", tk.END, values=result)

# Bind the select function to the tree view selection event
stud_table.bind("<<TreeviewSelect>>", select)



app.mainloop()
