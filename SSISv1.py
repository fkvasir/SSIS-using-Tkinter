import csv
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
    student_id = entry_id.get()
    student_age = entry_age.get()

    selected_courses = listbox_courses.curselection()

    if student_name and student_id and student_age and selected_courses:
        courses = [listbox_courses.get(index) for index in selected_courses]
        with open('student_courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_name] + courses + [student_age] + [student_id])
        
        messagebox.showinfo("Selection Saved", "Selection has been saved successfully.")
        entry_name.delete(0, tk.END)
        entry_id.delete(0,tk.END)
        entry_age.delete(0,tk.Entry)
        listbox_courses.selection_clear(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a student name, id and age and select at least one course.")

def remove_data():
    selected_index = listbox_data.curselection()

    if selected_index:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        
        if confirmation:
            with open('student_courses.csv', 'r') as file:
                records = list(csv.reader(file))
            
            del records[selected_index[0]]
            
            with open('student_courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)
            
            messagebox.showinfo("Data Removed", "Data has been removed successfully.")
            load_data()
    else:
        messagebox.showerror("Error", "Please select a record to remove.")

def load_data():
    listbox_data.delete(0, tk.END)

    with open('student_courses.csv', 'r') as file:
        records = csv.reader(file)
        for row in records:
            listbox_data.insert(tk.END, ', '.join(row))

def edit_data():
    selected_index = listbox_data.curselection()

    if selected_index:
        selected_data = listbox_data.get(selected_index)
        selected_data = selected_data.split(', ')

        window_edit = tk.Toplevel()
        window_edit.title("Edit Data")

        frame_edit = tk.Frame(window_edit)
        frame_edit.pack(pady=20)

        label_name = tk.Label(frame_edit, text="Student Name:")
        label_name.grid(row=0, column=0)
        entry_name = tk.Entry(frame_edit)
        entry_name.grid(row=0, column=1)
        entry_name.insert(tk.END, selected_data[0])

        label_courses = tk.Label(frame_edit, text="Courses:")
        label_courses.grid(row=1, column=0)
        entry_courses = tk.Entry(frame_edit)
        entry_courses.grid(row=1, column=1)
        entry_courses.insert(tk.END, ', '.join(selected_data[1:]))

        label_id = tk.Label(frame_edit,text="ID no.:")
        label_id.grid(row = 2, column = 0)
        entry_id = tk.Entry(frame_edit)
        entry_id.grid(row = 2, column = 1)
        entry_id.insert(tk.END, ', '.join(selected_data[2:]))

        label_age = tk.Label(frame_edit, text = "Age:" )
        label_age.grid(row = 3, column = 0)
        entry_age = tk.Entry(frame_edit)
        entry_age.grid(row = 3, column = 1)
        entry_age.insert(tk.END, ', '.join(selected_data[3:]))

        button_save = tk.Button(window_edit, text="Save Changes", command=lambda: save_changes(selected_index))
        button_save.pack(pady=10)

    else:
        messagebox.showerror("Error", "Please select a record to edit.")

def save_changes(selected_index):
    new_name = entry_name.get()
    new_courses = entry_course.get().split(', ')
    new_id = entry_id.get().split(', ')
    new_age = entry_age.get().split(', ')

    with open('student_courses.csv', 'r') as file:
        records = list(csv.reader(file))

    records[selected_index][0] = new_name
    records[selected_index][1:] = new_courses
    records[selected_index][2:] = new_id
    records[selected_index][3:] = new_age

    with open('student_courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

    messagebox.showinfo("Changes Saved", "Changes have been saved successfully.")
    entry_name.delete(0, tk.END)
    entry_courses.delete(0, tk.END)
    load_data()

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

label_name = tk.Label(frame_student, text="Student Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame_student)
entry_name.grid(row=0, column=1)

label_id = tk.Label(frame_student, text="Student ID no:")
label_id.grid(row=2, column=0)
entry_id = tk.Entry(frame_student)
entry_id.grid(row=2, column=1)

button_save_selection = tk.Button(root, text="Save Selection", command=save_selection)
button_save_selection.pack(pady=5)

listbox_data = tk.Listbox(root, width=50)
listbox_data.pack(pady=10)

label_age = tk.Label(frame_student, text="Enter Age:")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(frame_student)
entry_age.grid(row=3, column=1)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_remove_data = tk.Button(frame_buttons, text="Remove Data", command=remove_data)
button_remove_data.grid(row=0, column=0, padx=5)

button_edit_data = tk.Button(frame_buttons, text="Edit Data", command=edit_data)
button_edit_data.grid(row=0, column=1, padx=5)

load_data()

root.mainloop()
