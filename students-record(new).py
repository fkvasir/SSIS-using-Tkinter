import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = name_entry.get()
    course = course_entry.get()
    if name and course:
        students.append({'name': name, 'course': course})
        messagebox.showinfo('Success', 'Student added successfully!')
        clear_entries()
        update_student_listbox()
    else:
        messagebox.showerror('Error', 'Please enter both name and course.')

def edit_student():
    selected_index = student_listbox.curselection()
    if selected_index:
        selected_student = students[selected_index[0]]
        name = name_entry.get()
        course = course_entry.get()
        if name and course:
            selected_student['name'] = name
            selected_student['course'] = course
            messagebox.showinfo('Success', 'Student edited successfully!')
            clear_entries()
            update_student_listbox()
        else:
            messagebox.showerror('Error', 'Please enter both name and course.')
    else:
        messagebox.showerror('Error', 'Please select a student.')

def search_student():
    search_name = search_entry.get()
    if search_name:
        found_students = [student for student in students if search_name.lower() in student['name'].lower()]
        student_listbox.delete(0, tk.END)
        for student in found_students:
            student_listbox.insert(tk.END, student['name'])
    else:
        messagebox.showerror('Error', 'Please enter a name to search.')

def clear_entries():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

def update_student_listbox():
    student_listbox.delete(0, tk.END)
    for student in students:
        student_listbox.insert(tk.END, student['name'])

root = tk.Tk()
root.title('Student Management System')

# Student Listbox
student_listbox = tk.Listbox(root)
student_listbox.pack(side=tk.LEFT, padx=10)
student_listbox.bind('<<ListboxSelect>>', lambda event: populate_entries())

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
student_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=student_listbox.yview)

# Name Label and Entry
name_label = tk.Label(root, text='Name:')
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

# Course Label and Entry
course_label = tk.Label(root, text='Course:')
course_label.pack(pady=5)
course_entry = tk.Entry(root)
course_entry.pack()

# Search Label and Entry
search_label = tk.Label(root, text='Search:')
search_label.pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack()

# Buttons
add_button = tk.Button(root, text='Add Student', command=add_student)
add_button.pack(pady=5)

edit_button = tk.Button(root, text='Edit Student', command=edit_student)
edit_button.pack(pady=5)

search_button = tk.Button(root, text='Search Student', command=search_student)
search_button.pack(pady=5)

def populate_entries():
    selected_index = student_listbox.curselection()
    if selected_index:
        selected_student = students[selected_index[0]]
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, selected_student['name'])
        course_entry.delete(0, tk.END)
        course_entry.insert(tk.END, selected_student['course'])

root.mainloop()
