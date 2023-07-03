import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox




  
app = tk.Tk()
app.geometry("1300x650")
app.title("SSIS version 2.0")




# placeholders for entries
# __init__ variables
id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
course =tk.StringVar()
searchin = tk.StringVar()
coursecode=tk.StringVar()

# placeholder values
def setph(word,num):
    if num == 1:
        id.set(word)
    if num == 2:
        name.set(word)
    if num == 3:
        sex.set(word)
    if num == 4:
        year.set(word)
    if num == 5:
        course.set(word)
    if num == 6:
        searchin.set(word)
    if num == 7:
        coursecode.set(word)
        
def read():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add(name, id_number, gender, year_level, course):
    id_number = id.get()
    name = name.get()
    gender = sex.get()
    year_level = year.get()
    course = course.get()

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
            sex_entry.delete(0, tk.END)
            sex_entry.insert(tk.END, selected_data[2])
            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, selected_data[3])
            course_entry.delete(0, tk.END)
            course_entry.insert(tk.END, selected_data[4])
        
    except:
        messagebox.showinfo("Error","Please select a data row")
        
        
def update():
    selected_id = id_entry.get()
    new_name = name_entry.get()
    new_sex = sex_entry.get()
    new_year = year_entry.get()
    new_course = course_entry.get()


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute('''UPDATE students SET name=?, sex=?, year=?, course=? WHERE id_number=?''',
                   (new_name, new_sex, new_year, new_course, selected_id))

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data updated successfully.")
    else:
        messagebox.showinfo("Error", "No matching student found.")

    # Clear the entry fields
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    refresh_data()

# Function to refresh the data in the tree view
def refresh_data():
    # Clear the tree view
    for item in stud_table.get_children():
        stud_table.delete(item)
    
    results = read()

    for result in results:
        stud_table.insert("", tk.END, values=result)
    
    
        

def search():
    search_term = searchin.get()    

    # Connect to the database
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Execute the search query
    cursor.execute("SELECT * FROM students WHERE id LIKE ? OR name LIKE ? OR sex LIKE ? OR year LIKE ? OR course LIKE ?",
                   (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))

    results = cursor.fetchall()

    # Clear the tree view
    stud_table.delete(*stud_table.get_children())

    # Insert the search results into the tree view
    for result in results:
        stud_table.insert("", tk.END, values=result)

    conn.close()
    
def add_course(course_code, course_name):
    course_code = coursecode_entry.get()
    course_name = course_entry.get()
    
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    # Check if the course already exists in the database
    cursor.execute("SELECT * FROM courses WHERE course_code = ?", (course_code,))
    existing_course = cursor.fetchone()
    if existing_course:
        messagebox.showinfo("Error", "Course already exists.")
        return
    
    # Insert the new course into the database
    cursor.execute("INSERT INTO courses (course_code, course_name) VALUES (?, ?)", (course_code, course_name))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Course added successfully.")

def update_course(course_code, new_course_name):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    # Check if the course exists in the database
    cursor.execute("SELECT * FROM courses WHERE course_code = ?", (course_code,))
    existing_course = cursor.fetchone()
    if not existing_course:
        messagebox.showinfo("Error", "Course does not exist.")
        return
    
    # Update the course name in the database
    cursor.execute("UPDATE courses SET course_name = ? WHERE course_code = ?", (new_course_name, course_code))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Course updated successfully.")

def delete_course(course_code):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    # Check if the course exists in the database
    cursor.execute("SELECT * FROM courses WHERE course_code = ?", (course_code,))
    existing_course = cursor.fetchone()
    if not existing_course:
        messagebox.showinfo("Error", "Course does not exist.")
        return
    
    # Delete the course from the database
    cursor.execute("DELETE FROM courses WHERE course_code = ?", (course_code,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Course deleted successfully.")

def search_course(search_term):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    # Execute the search query
    cursor.execute("SELECT * FROM courses WHERE course_code LIKE ? OR course_name LIKE ?",
                   (f"%{search_term}%", f"%{search_term}%"))

    results = cursor.fetchall()
    conn.close()
    return results




# Graphical User Interface

title_label = tk.Label(app, border=5, height=20, relief= tk.GROOVE, bg = "lightblue")
title_label.pack(side=tk.TOP,fill=tk.X)

# frames
detail_frame = tk.LabelFrame(app, bd=10,relief=tk.GROOVE,bg="lightblue")
detail_frame.place(x=20,y=55,width=450,height=575)

data_frame = tk.Frame(app, bg="lightblue",relief=tk.GROOVE)
data_frame.place(x=475,y=55,width=810,height=575)




# entries and labels >> detail frame
id_label = tk.Label(detail_frame, text="ID",font=("Times", 10), bg= "lightblue")
id_label.place(x=20,y=20)
id_entry = tk.Entry(detail_frame,bd=5,font=("Times",10),textvariable=id)
id_entry.place(x=110,y=20)

name_label = tk.Label(detail_frame, text="Name",font=("Times", 10), bg= "lightblue")
name_label.place(x=20,y=60)
name_entry = tk.Entry(detail_frame,bd=5,font=("Times",10),textvariable=name)
name_entry.place(x=110, y=60)

sex_label = tk.Label(detail_frame, text="Sex",font=("Times", 10), bg= "lightblue")
sex_label.place(x=20,y=110)
sex_entry = ttk.Combobox(detail_frame,font=("Times",8),textvariable=sex,)
sex_entry['values']=("Male","Female")
sex_entry.place(x=110,y=110)


year_label = tk.Label(detail_frame, text="Year level",font=("Times",10),bg="lightblue")
year_label.place(x=20,y=400)
year_entry = tk.Entry(detail_frame,bd=5,font=("Times",10),textvariable=year)
year_entry.place(x=110,y=400)


# Courses
course_label = tk.Label(detail_frame, text="Course Name",bg="lightblue",bd=5,font=("Times",10),width=10)
course_label.place(x=20,y=150)
coursecode_entry= tk.Label(detail_frame, text="Course Code",bg="lightblue",bd=5,font=("Times",10))
coursecode_entry.place(x=20,y=200)

course_entry = tk.Entry(detail_frame,bd=5,font=("Times",10),textvariable=course)
course_entry.place(x=110,y=150)
coursecode_entry = tk.Entry(detail_frame,bd=5,font=("Times",10),textvariable=coursecode)
coursecode_entry.place(x=110, y=200)


button_add_course = tk.Button(detail_frame, text="Add Course",bg="lightgrey",bd=5,font=("Times",7),width=10, command=add_course)
button_add_course.place(x=342,y=167)





# button frame
btn_frame= tk.Frame(detail_frame, bg="lightgrey",bd=10,relief=tk.GROOVE)
btn_frame.place(x=120,y=460,width=230,height=55)

# buttons >> btn frame
add_btn = tk.Button(btn_frame, text="Add",bg="lightgrey",bd=5,font=("Times",7),width=15, command=add)
add_btn.grid(row=0,column=0,padx=7,pady=2)


delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete",bd=5,font=("Times",7),width=15,command=delete )
delete_btn.grid(row=0,column=1,padx=7,pady=2)




# top right frame
search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

# search and show buttons
search_label=tk.Label(title_label,text="Search",bg="lightblue",font=("Times",17))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_entry =ttk.Entry(title_label,font=("Times", 15),textvariable=searchin)
search_entry.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(title_label,bg="lightgrey",text="Search",bd=5,font=("Times",7),width=15,command=search)
search_btn.place(x=880,y=5)

update_button = tk.Button(title_label, bg="lightgrey", text="Edit",bd=5,font=("Times",7),width=15,command=update)
update_button.place(x=980,y=5)

reset_btn = tk.Button(title_label, text="Reset",bg="lightgrey", bd=5,font=("Times",7),width=15, command=reset_data)
reset_btn.place(x=1080,y=5)


# frame for treeview
main_frame=tk.Frame(data_frame,bg="lightgrey", bd=7,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient = tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient = tk.HORIZONTAL)

# style object
style = ttk.Style()
style.configure("Treeview", bd= 7)

# Treeview
stud_table = ttk.Treeview(main_frame)
stud_table["columns"] = ("ID", "Name", "Sex", "Year Level", "Course")
stud_table.column("ID", anchor="center", width=100, minwidth=50)
stud_table.column("Name", anchor="center", width=150, minwidth=100)
stud_table.column("Sex", anchor="center", width=80, minwidth=50)
stud_table.column("Year Level", anchor="center", width=100, minwidth=50)
stud_table.column("Course", anchor="center", width=200, minwidth=100)

stud_table.heading("ID", text="ID")
stud_table.heading("Name", text="Name")
stud_table.heading("Sex", text="Sex")
stud_table.heading("Year Level", text="Year Level")
stud_table.heading("Course", text="Course")
stud_table.column("#0", width=0, stretch=tk.NO)  # Remove space before "ID" column
stud_table.pack(fill=tk.BOTH, expand=True)

# Populate the tree view with data
results = read()
for result in results:
    stud_table.insert("", tk.END, values=result)

# Bind the select function to the tree view selection event
stud_table.bind("<<TreeviewSelect>>", select)



app.mainloop()
