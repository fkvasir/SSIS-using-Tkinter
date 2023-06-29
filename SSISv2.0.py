import sqlite3
import tkinter as tk
from tkinter import messagebox

def add_course():
    course = entry_course.get()

    if course:
        listbox_courses.insert(tk.END, course)
        entry_course.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a course.")

def save_selection():
    student_name = entry_name.get()
    selected_courses = listbox_courses.curselection()

    if student_name and selected_courses:
        courses = [listbox_courses.get(index) for index in selected_courses]
        with sqlite3.connect('student_courses.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO student_courses (name, courses) VALUES (?, ?)", (student_name, ', '.join(courses)))
        
        messagebox.showinfo("Selection Saved", "Selection has been saved successfully.")
        entry_name.delete(0, tk.END)
        listbox_courses.selection_clear(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a student name and select at least one course.")

def remove_data():
    selected_index = listbox_data.curselection()

    if selected_index:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        
        if confirmation:
            with sqlite3.connect('student_courses.db') as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM student_courses WHERE rowid=?", (selected_index[0]+1,))
            
            messagebox.showinfo("Data Removed", "Data has been removed successfully.")
            load_data()
    else:
        messagebox.showerror("Error", "Please select a record to remove.")

def load_data():
    listbox_data.delete(0, tk.END)

    with sqlite3.connect('student_courses.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student_courses")
        records = cursor.fetchall()
        for row in records:
            listbox_data.insert(tk.END, f"Name: {row[0]}, Courses: {row[1]}")

def edit_data():
    selected_index = listbox_data.curselection()

    if selected_index:
        selected_data = listbox_data.get(selected_index)
        selected_data = selected_data.split(', ')
        selected_name = selected_data[0][6:]
        selected_courses = selected_data[1][9:].split(', ')

        window_edit = tk.Toplevel()
        window_edit.title("Edit Data")

        frame_edit = tk.Frame(window_edit)
        frame_edit.pack(pady=20)

        label_name = tk.Label(frame_edit, text="Student Name:")
        label_name.grid(row=0, column=0)
        entry_name = tk.Entry(frame_edit)
        entry_name.grid(row=0, column=1)
        entry_name.insert(tk.END, selected_name)

        label_courses = tk.Label(frame_edit, text="Courses:")
        label_courses.grid(row=1, column=0)
        entry_courses = tk.Entry(frame_edit)
        entry_courses.grid(row=1, column=1)
        entry_courses.insert(tk.END, ', '.join(selected_courses))

        button_save = tk.Button(window_edit, text="Save Changes", command=lambda: save_changes(selected_index))
        button_save.pack(pady=10)

    else:
        messagebox.showerror("Error", "Please select a record to edit.")

def save_changes(selected_index):
    new_name = entry_name.get()
    new_courses = entry_courses.get().split(', ')

    with sqlite3.connect('student_courses.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE student_courses SET name=?, courses=? WHERE rowid=?", (new_name, ', '.join(new_courses), selected_index[0]+1))

    messagebox.showinfo("Changes Saved", "Changes have been saved successfully.")
    entry_name.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    load_data()

# Create database and table if they don't exist
with sqlite3.connect('student_courses.db') as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS student_courses (name TEXT, courses TEXT)")

root = tk.Tk()
root.title("Course Selection")

frame_courses = tk.Frame(root)
frame_courses.pack(pady=20)

label_course = tk.Label(frame_courses, text="Enter Course:")
label_course.grid(row=0, column=0)
entry_course = tk.Entry(frame_courses)
entry_course.grid(row=0, column=1)

button_add_course = tk.Button(root, text="Add Course", command=add_course)
button_add_course.pack(pady=5)

listbox_courses = tk.Listbox(root, width=50)
listbox_courses.pack(pady=10)

frame_student = tk.Frame(root)
frame_student.pack(pady=20)

label_name = tk.Label(frame_student, text="Enter Student Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame_student)
entry_name.grid(row=0, column=1)

button_save_selection = tk.Button(root, text="Save Selection", command=save_selection)
button_save_selection.pack(pady=5)

listbox_data = tk.Listbox(root, width=50)
listbox_data.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_remove_data = tk.Button(frame_buttons, text="Remove Data", command=remove_data)
button_remove_data.grid(row=0, column=0, padx=5)

button_edit_data = tk.Button(frame_buttons, text="Edit Data", command=edit_data)
button_edit_data.grid(row=0, column=1, padx=5)

load_data()

root.mainloop()
