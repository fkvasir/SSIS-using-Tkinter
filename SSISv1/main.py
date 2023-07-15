import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



root = tk.Tk()
root.title("SSIS v1.0")
root.geometry("990x630")

title_label = tk.Label(root,height=3,relief=tk.GROOVE,bg="lightblue")
title_label.pack(side=tk.TOP,fill=tk.X)

# frames
detail_frame = tk.LabelFrame(root,font=("Times",13),bd=5,relief=tk.GROOVE,bg="lightblue")
detail_frame.place(y=35,width=430,height=586)

data_frame = tk.Frame(root,bg="lightblue",bd=5,relief=tk.GROOVE)
data_frame.place(x=429,y=35,width=550,height=586)

# __init__ variables
id= tk.StringVar()
name=tk.StringVar()
sex=tk.StringVar()
year=tk.StringVar()
search=tk.StringVar()
course =tk.StringVar()

# backend functions
def add_course():
    course = entry_course.get()

    if course:
        listbox_courses.insert(tk.END, course)
        entry_course.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a course.")

def save_selection():
    student_name = entry_name.get()
    student_id = entry_id.get()
    student_sex = entry_sex.get()
    student_year = entry_year.get()

    selected_courses = listbox_courses.curselection()

    if student_name and student_id and student_sex and selected_courses and student_year:
        courses = [listbox_courses.get(index) for index in selected_courses]
        with open('student_courses.csv', 'a', newline='') as file:
            writer = csv.writer(
                file
            )
            writer.writerow([student_id] + [student_name]  + [student_sex] + courses + [student_year])
            load_data()
        
        messagebox.showinfo("Selection Saved", "Selection has been saved successfully.")

    else:
        messagebox.showerror("Error", "Please enter a student name, id, sex and year level and select at most one course.")

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
    else:
        messagebox.showerror("Error", "Please select a record to remove.")
        
        
def load_data():
    dataview.delete(0, tk.END)

    with open('student_courses.csv', 'r') as file:
        records = csv.reader(file)
        for row in records:
            dataview.insert(tk.END, ', '.join(row))

def edit_data():
    selected_index = dataview.selection()

    if selected_index:
        selected_data = dataview.item(dataview.selection())['values']

        window_edit = tk.Toplevel()
        window_edit.title("Edit Data")

        frame_edit = tk.Frame(window_edit)
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

        button_save = tk.Button(window_edit, text="Save Changes", command=lambda: save_changes(selected_index, entry_edit_name, entry_edit_courses, entry_edit_sex, entry_edit_id, entry_edit_year))
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
    if 'window_edit' in globals() and isinstance(window_edit, tk.Toplevel):
        window_edit.destroy()

    
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
        # If the search entry is empty, load all data
        load_data()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_sex.delete(0,tk.END)
    entry_id.delete(0,tk.END)
    entry_year.delete(0,tk.END)
    listbox_courses.selection_clear(0, tk.END)

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
        listbox_courses.delete(0, tk.END)
        for course in selected_data[3].split(', '):
            listbox_courses.insert(tk.END, course)

    except IndexError:
        pass

# Create TreeView widget
dataview = ttk.Treeview(data_frame, columns=("ID", "Name", "Sex", "Course", "Year"), show="headings", selectmode="browse")
dataview.heading("ID", text="ID")
dataview.heading("Name", text="Name")
dataview.heading("Sex", text="Sex")
dataview.heading("Course", text="Course")
dataview.heading("Year", text="Year")

dataview.column("ID",anchor="center", width=120)
dataview.column("Name",anchor="w", width=120)
dataview.column("Sex",anchor="center", width=80)
dataview.column("Course",anchor="center", width=120)
dataview.column("Year",anchor="center", width=70)

dataview.pack(expand=True, fill=tk.BOTH)

# Bind the dataview to the function that will populate the entry fields when a row is selected
dataview.bind("<ButtonRelease-1>", get_selected_row)

# labels and entries >>>detail frame
label_id = tk.Label(detail_frame, text="ID no.",font=("Times", 13), bg= "lightblue")
label_id.grid(row=0,column=0,padx=2,pady=20)
entry_id = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=id)
entry_id.grid(row=0,column=1,padx=2,pady=2)


label_name = tk.Label(detail_frame, text="Name",font=("Times", 13), bg= "lightblue")
label_name.grid(row=1,column=0,padx=2,pady=10)
entry_name = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=name)
entry_name.grid(row=1 ,column=1,padx=2,pady=10)

menu_button = tk


sex_label = tk.Label(detail_frame, text="Sex",font=("Times", 13), bg= "lightblue")
sex_label.grid(row=2,column=0,padx=2,pady=10)
entry_sex = ttk.Combobox(detail_frame,font=("Times",11),textvariable=sex,)
entry_sex['values']=("Male","Female")
entry_sex.grid(row=2,column=1,padx=2,pady=10)

# listbox << added course
listbox_courses = tk.Listbox(detail_frame, width=50,bd=7)
listbox_courses.grid(row=4,column=1,padx=2,pady=10)

label_course = tk.Label(detail_frame, text="Course", font=("Times",13),bg="lightblue")
label_course.grid(row=3, column=0,padx=1,pady=10)
entry_course = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=course)
entry_course.grid(row=3, column=1, padx=1, pady=10)


label_year = tk.Label(detail_frame, text="Year level:",font=("Times",13),bg="lightblue")
label_year.grid(row=6, column=0,pady=10)
entry_year = tk.Entry(detail_frame,bd=7,font=("Times",13),textvariable=year)
entry_year.grid(row=6, column=1,pady=10)

# >> add course to listbox
button_add_course = tk.Button(detail_frame, text="Add Course",bg="lightblue",bd=7,font=("Times",7),width=10, command=add_course)
button_add_course.place(x=342,y=178)

# buttons >> button frame
btn_frame= tk.Frame(detail_frame, bg="lightblue",bd=10,relief=tk.GROOVE)
btn_frame.place(x=120,y=490,width=240,height=55)


button_save_selection = tk.Button(btn_frame, text="Save",bg="lightblue",bd=7,font=("Times",7),width=15, command=save_selection)
button_save_selection.grid(row=0,column=0,padx=7,pady=2)


clear_btn = tk.Button(btn_frame, bg="lightblue", text="Clear",bd=7,font=("Times",7),width=15, command=clear_entries)
clear_btn.grid(row=0,column=1,padx=7,pady=2)


# search and show buttons
search_label=tk.Label(title_label,text="Search",bg="lightblue",font=("Times",14))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_entry =ttk.Entry(title_label,font=("Times", 15),textvariable=search)
search_entry.grid(row=0,column=1,padx=12,pady=2)



# buttons >> search_frame
button_remove_data = tk.Button(title_label, text="Remove Data", bg="lightblue", bd=7, font=("Arial", 7), width=15, command=remove_data)
button_remove_data.place(x=655, y=2)

search_btn = tk.Button(title_label, bg="lightblue", text="Search", bd=7, font=("Arial", 7), width=15, command=search_data)
search_btn.place(x=540, y=2)

button_edit_data = tk.Button(title_label, bg="lightblue", text="Edit", bd=7, font=("Arial", 7), width=15, command=edit_data)
button_edit_data.place(x=770, y=2)


load_data()

root.mainloop()
