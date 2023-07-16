import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



root = tk.Tk()
root.title("SSIS v1.0")
root.geometry("1280x700")

title_label = tk.Label(root,height=3,relief=tk.GROOVE,bg="lightgreen")
title_label.pack(side=tk.TOP,fill=tk.X)

# frames
detail_frame = tk.LabelFrame(root,font=("Times",13),bd=5,relief=tk.GROOVE,bg="lightgreen")
detail_frame.place(y=35,width=430,height=660)

data_frame = tk.Frame(root,bg="lightgreen",bd=5,relief=tk.GROOVE)
data_frame.place(x=429,y=35,width=850,height=660)

# __init__ variables
id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
search=tk.StringVar()
courseID =tk.StringVar()
courseName=tk.StringVar()

# backend functions
courses_tree = None
  

def add_course():
    global courses_tree  # Add this line to access the global variable

    course_id = entry_course_id.get()
    course_name = entry_course_name.get()

    if course_id and course_name:
        courses_tree.insert("", "end", values=(course_id, course_name))
        entry_course_id.delete(0, tk.END)
        entry_course_name.delete(0, tk.END)

        # Save the new course to the 'courses.csv' file
        with open('courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([course_id, course_name])
    else:
        messagebox.showerror("Error", "Please enter both Course ID and Course Name.")

def load_courses():
    global courses_tree

    try:
        with open('courses.csv', 'r') as file:
            records = csv.reader(file)
            for row in records:
                courses_tree.insert("", "end", values=row)
    except FileNotFoundError:
        messagebox.showerror("Error", "The 'courses.csv' file does not exist.")
        root.destroy()                
        
def save_selection():
    student_name = entry_name.get()
    student_id = entry_id.get()
    student_sex = entry_sex.get()
    student_year = entry_year.get()

    selected_courses = courses_tree.selection()

    if student_name and student_id and student_sex and selected_courses and student_year:
        courses = [courses_tree.item(item, 'values') for item in selected_courses]
        # Extract only the Course IDs and join them into a comma-separated string
        course_ids = ", ".join([course[0] for course in courses])
        with open('student_courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, student_name, student_sex, course_ids, student_year])
        load_data()

        messagebox.showinfo("Selection Saved", "Selection has been saved successfully.")
    else:
        messagebox.showerror("Error", "Please enter a student name, id, sex and year level and select at least one course.")



def remove_data():
    selected_items = dataview.selection()

    if selected_items:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")

        if confirmation:
            with open('student_courses.csv', 'r') as file:
                records = list(csv.reader(file))

            indices_to_remove = [dataview.index(item) for item in selected_items]
            indices_to_remove.sort(reverse=True)  # Sort in reverse order to delete from the end

            for index in indices_to_remove:
                del records[index]

            with open('student_courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)

            messagebox.showinfo("Data Removed", "Data has been removed successfully.")
            load_data()
            clear_entries()
    else:
        messagebox.showerror("Error", "Please select a record to remove.")        
        
def load_data():
    dataview.delete(*dataview.get_children())  # Clear existing data

    with open('student_courses.csv', 'r') as file:
        records = csv.reader(file)
        for row in records:
            # Remove brackets and quotation marks from the courseIDs
            course_ids = row[3].replace(" ", "").strip("[]").split(",") if row[3] else []
            dataview.insert("", "end", values=(row[0], row[1], row[2], ", ".join(course_ids), row[4]))

def edit_data():
    global edit_window
    selected_index = dataview.selection()

    if selected_index:
        selected_data = dataview.item(dataview.selection())['values']

        edit_window = tk.Toplevel()
        edit_window.title("Edit Data")

        frame_edit = tk.Frame(edit_window)
        frame_edit.pack(pady=20)

        label_name = tk.Label(frame_edit, text="Name")
        label_name.grid(row=0, column=0)
        entry_edit_name = tk.Entry(frame_edit)
        entry_edit_name.grid(row=0, column=1)
        entry_edit_name.insert(tk.END, selected_data[1])  # Index 1 is the Name

        label_courses = tk.Label(frame_edit, text="Courses")
        label_courses.grid(row=1, column=0)
        entry_edit_courses = tk.Entry(frame_edit)
        entry_edit_courses.grid(row=1, column=1)
        entry_edit_courses.insert(tk.END, selected_data[3])  # Index 3 is the Courses

        label_id = tk.Label(frame_edit, text="ID")
        label_id.grid(row=2, column=0)
        entry_edit_id = tk.Entry(frame_edit)
        entry_edit_id.grid(row=2, column=1)
        entry_edit_id.insert(tk.END, selected_data[0])  # Index 2 is the Sex

        label_sex = tk.Label(frame_edit, text="Sex")
        label_sex.grid(row=3, column=0)
        entry_edit_sex = tk.Entry(frame_edit)
        entry_edit_sex.grid(row=3, column=1)
        entry_edit_sex.insert(tk.END, selected_data[2])  # Index 0 is the ID

        label_year = tk.Label(frame_edit, text="Year")
        label_year.grid(row=4, column=0)
        entry_edit_year = tk.Entry(frame_edit)
        entry_edit_year.grid(row=4, column=1)
        entry_edit_year.insert(tk.END, selected_data[4])  # Index 4 is the Year

        button_save = tk.Button(edit_window, text="Save Changes",
                                command=lambda: save_changes(selected_index, entry_edit_name, entry_edit_courses,
                                                             entry_edit_sex, entry_edit_id, entry_edit_year))
        button_save.pack(pady=10)

    else:
        messagebox.showerror("Error", "Please select a record to edit.")
                
def save_changes(selected_index, entry_name, entry_courses, entry_sex, entry_id, entry_year):
    new_name = entry_name.get()
    new_courses = entry_courses.get().split(', ')
    new_sex = entry_sex.get()
    new_id = entry_id.get()
    new_year = entry_year.get()

    with open('student_courses.csv', 'r') as file:
        records = list(csv.reader(file))

    selected_indices = [dataview.index(item) for item in selected_index]

    if selected_indices:
        for index in selected_indices:
            records[index][0] = new_id
            records[index][1] = new_name
            records[index][2] = new_sex
            records[index][3] = ', '.join(new_courses)
            records[index][4] = new_year

    with open('student_courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

    messagebox.showinfo("Changes Saved", "Changes have been saved successfully.")
    entry_name.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    entry_sex.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    load_data()
    clear_entries()
    edit_window.destroy()    

def search_data():
    search_term = search_entry.get().lower()

    if search_term:
        dataview.delete(*dataview.get_children())

        with open('student_courses.csv', 'r') as file:
            records = csv.reader(file)
            found_records = []

            for row in records:
                for field in row:
                    if search_term in field.lower():
                        found_records.append(row)
                        break

            for record in found_records:
                dataview.insert("", "end", values=record)

        if not found_records:
            messagebox.showinfo("Search Result", "No matching records found.")
    else:
        # If the search bar is empty, load all data
        load_data()
        clear_entries()
        

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_course_id.delete(0, tk.END)
    entry_sex.delete(0,tk.END)
    entry_id.delete(0,tk.END)
    entry_year.delete(0,tk.END)
    entry_course_name.delete(0, tk.END)

def load_data():
    dataview.delete(*dataview.get_children())  # Clear existing data

    with open('student_courses.csv', 'r') as file:
        records = csv.reader(file)
        for row in records:
            dataview.insert("", "end", values=row)


# Function to get the selected row from the dataview
def get_selected_row(event):
    try:
        selected_item = dataview.focus()
        selected_data = dataview.item(selected_item, 'values')
        entry_id.delete(0, tk.END)
        entry_id.insert(tk.END, selected_data[0])
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, selected_data[1])
        entry_sex.set(selected_data[2])
        entry_year.delete(0, tk.END)
        entry_year.insert(tk.END, selected_data[4])

        # Clear and populate the listbox_courses with the courses of the selected row
        courses_tree.selection_set(courses_tree.index(courses_tree.identify_region(event.x, event.y)))
    except IndexError:
        pass

def get_selected_course(event):
    selected_item = courses_tree.focus()
    selected_data = courses_tree.item(selected_item, 'values')
    
    # Set the values to the corresponding entry widgets
    courseID.set(selected_data[0])
    courseName.set(selected_data[1])
    

# Create TreeView widget
dataview = ttk.Treeview(data_frame, columns=("ID", "Name", "Sex", "Course", "Year"), show="headings", selectmode="browse")
dataview.heading("ID", text="ID")
dataview.heading("Name", text="Name")
dataview.heading("Sex", text="Sex")
dataview.heading("Course", text="Course")
dataview.heading("Year", text="Year")

dataview.column("ID",anchor="center", width=120)
dataview.column("Name",anchor="w", width=170)
dataview.column("Sex",anchor="center", width=80)
dataview.column("Course",anchor="center", width=150)
dataview.column("Year",anchor="center", width=70)
dataview.pack(expand=True, fill=tk.BOTH)

dataview.bind("<ButtonRelease-1>", get_selected_row)

# Courses Treeview
courses_tree = ttk.Treeview(detail_frame, columns=("CourseID", "CourseName"), show="headings", selectmode="browse")
courses_tree.heading("CourseID", text="Course ID")
courses_tree.heading("CourseName", text="Course Name")

courses_tree.column("CourseID", anchor="center", width=80)
courses_tree.column("CourseName", anchor="center", width=150)
courses_tree.place(x=95, y=285)
courses_tree.bind("<<TreeviewSelect>>", get_selected_course)
load_courses()


# labels and entries >>>detail frame
label_id = tk.Label(detail_frame, text="ID no.",font=("Times", 13), bg= "lightgreen")
label_id.grid(row=0,column=0,padx=2,pady=20)
entry_id = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=id)
entry_id.grid(row=0,column=1,padx=2,pady=2)


label_name = tk.Label(detail_frame, text="Name",font=("Times", 13), bg= "lightgreen")
label_name.grid(row=1,column=0,padx=2,pady=10)
entry_name = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=name)
entry_name.grid(row=1 ,column=1,padx=2,pady=10)


menu_button = tk


sex_label = tk.Label(detail_frame, text="Sex",font=("Times", 13), bg= "lightgreen")
sex_label.grid(row=2,column=0,padx=2,pady=10)
entry_sex = ttk.Combobox(detail_frame,font=("Times",11),textvariable=sex,)
entry_sex['values']=("Male","Female")
entry_sex.grid(row=2,column=1,padx=2,pady=10)



# Labels and Entries for Course
label_course_id = tk.Label(detail_frame, text="Course ID", font=("Times", 13), bg="lightgreen")
label_course_id.grid(row=3,column=0, padx=1,pady=10)
entry_course_id = tk.Entry(detail_frame, bd=7, font=("Times", 13),textvariable=courseID)
entry_course_id.grid(row=3, column=1,padx=1,pady=10)

label_course_name = tk.Label(detail_frame, text="Course Name", font=("Times", 13), bg="lightgreen")
label_course_name.grid(row=4, column=0, padx=1, pady=10)
entry_course_name = tk.Entry(detail_frame, bd=7, font=("Times", 13),textvariable=courseName)
entry_course_name.grid(row=4, column=1, padx=1, pady=10)


label_year = tk.Label(detail_frame, text="Year level",font=("Times",13),bg="lightgreen")
label_year.place(x=10,y=530)
entry_year = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=year)
entry_year.place(x=105,y=525)

# >> add course to listbox
button_add_course = tk.Button(detail_frame, text="Add Course",bd=7,font=("Times",7),width=10, command=add_course)
button_add_course.place(x=342,y=178)

# buttons >> button frame
btn_frame= tk.Frame(detail_frame, bg="lightgreen",bd=10,relief=tk.GROOVE)
btn_frame.place(x=150,y=580,width=130,height=55)


button_save_selection = tk.Button(btn_frame, text="Save",bd=7,font=("Times",7),width=15, command=save_selection)
button_save_selection.grid(row=0,column=0,padx=7,pady=2)


# search and show buttons
search_label=tk.Label(title_label,text="Search",bg="lightgreen",font=("Times",14))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_entry =ttk.Entry(title_label,font=("Times", 15),textvariable=search)
search_entry.grid(row=0,column=1,padx=12,pady=2)


# buttons >> search_frame
button_remove_data = tk.Button(title_label, text="Remove Data", bd=7, font=("Arial", 7), width=15, command=remove_data)
button_remove_data.place(x=1025, y=2)

search_btn = tk.Button(title_label, text="Search", bd=7, font=("Arial", 7), width=15, command=search_data)
search_btn.place(x=910, y=2)

button_edit_data = tk.Button(title_label, text="Edit", bd=7, font=("Arial", 7), width=15, command=edit_data)
button_edit_data.place(x=1140, y=2)

load_data()

root.mainloop()
