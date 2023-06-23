import tkinter as tk
import customtkinter
import csv
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("SSIS version 1")

title = customtkinter.CTkLabel(app, text = "Simple Student Information System")
title.pack(padx=10, pady= 10)


frame_add_courses = customtkinter.CTkFrame(app)
frame_add_courses.pack(pady=20)

label_course = customtkinter.CTkLabel(frame_add_courses, text="Enter Course:")
label_course.grid(row=0, column=0)
entry_course = customtkinter.CTkEntry(frame_add_courses)
entry_course.grid(row=0, column=1)

button_add_course = customtkinter.CTkButton(frame_add_courses, text="Add Course")
button_add_course.pack(pady=5)

button_show_courses = customtkinter.CTkButton(frame_add_courses, text="Show Courses")
button_show_courses.pack(pady=5)


frame_student = customtkinter.CTkFrame(app)
frame_student.pack(pady=20)

label_name = customtkinter.CTkLabel(frame_student, text="Enter Student Name:")
label_name.grid(row=0, column=0)
entry_name = customtkinter.CTkEntry(frame_student)
entry_name.grid(row=0, column=1)

button_save_selection = customtkinter.CTkButton(app, text="Save Selection")
button_save_selection.pack(pady=5)

# listbox_data = customtkinter.CTkListBox(app, width=50)
# listbox_data.pack(pady=10)

frame_buttons = customtkinter.CTkFrame(app)
frame_buttons.pack(pady=10)

button_remove_data = customtkinter.CTkButton(frame_buttons, text="Remove Data")
button_remove_data.grid(row=0, column=0, padx=5)

button_edit_data = customtkinter.CTkButton(frame_buttons, text="Edit Data")
button_edit_data.grid(row=0, column=1, padx=5)

frame_search = customtkinter.CTkFrame(app)
frame_search.pack(pady=20)

label_search = customtkinter.CTkLabel(frame_search, text="Search:")
label_search.grid(row=0, column=0)
entry_search = customtkinter.CTkEntry(frame_search)
entry_search.grid(row=0, column=1)

button_search = customtkinter.CTkButton(app, text="Search")
button_search.pack(pady=5)

def add_course():
    course = entry_course.get()

    if course:
        with open('courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([course])
        
        messagebox.showinfo("Course Added", "Course has been added successfully.")
        entry_course.delete(0, tk.END)
    else:
        CTkMessagebox(title="Error", message = "Something went wrong", icon="cancel")

def show_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        courses = [row[0] for row in reader]
    
    CTkMessagebox("Courses", "\n".join(courses))

def save_selection():
    student_name = entry_name.get()
    selected_courses = listbox_courses.get_selected_items()

    if student_name and selected_courses:
        with open('student_courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_name] + selected_courses)
        
        messagebox.showinfo("Selection Saved", "Selection has been saved successfully.")
        entry_name.delete(0, tk.END)
        listbox_courses.clear_selection()
    else:
        messagebox.showerror("Error", "Please enter a student name and select at least one course.")

def remove_data():
    selected_data = listbox_data.get_selected_items()

    if selected_data:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        
        if confirmation:
            with open('student_courses.csv', 'r') as file:
                records = list(csv.reader(file))
            
            with open('student_courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in records:
                    if row != selected_data:
                        writer.writerow(row)
            
            messagebox.showinfo("Data Removed", "Data has been removed successfully.")
            load_data()
    else:
        messagebox.showerror("Error", "Please select a record to remove.")

def load_data():
    listbox_data.clear()
    with open('student_courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            listbox_data.insert(row)

def edit_data():
    selected_data = listbox_data.get_selected_items()

    if selected_data:
        selected_name = selected_data[0]
        selected_courses = selected_data[1:]

        window_edit = customtkinter.CTk()
        window_edit.title("Edit Data")

        frame_edit = customtkinter.CTkFrame(window_edit)
        frame_edit.pack(pady=20)
        
        label_name = customtkinter.CTkLabel(frame_edit, text="Student Name:")
        label_name.grid(row=0, column=0)
        entry_name = customtkinter.CTkEntry(frame_edit)
        entry_name.grid(row=0, column=1)
        entry_name.set_text(selected_name)

        label_courses = customtkinter.CTkLabel(frame_edit, text="Courses:")
        label_courses.grid(row=1, column=0)
        entry_courses = customtkinter.CTkEntry(frame_edit)
        entry_courses.grid(row=1, column=1)
        entry_courses.set_text(', '.join(selected_courses))

        def save_changes():
            new_name = entry_name.get_text()
            new_courses = entry_courses.get_text().split(', ')
            updated_data = [new_name] + new_courses

            with open('student_courses.csv', 'r') as file:
                records = list(csv.reader(file))
            
            with open('student_courses.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in records:
                    if row != selected_data:
                        writer.writerow(row)
                writer.writerow(updated_data)

            messagebox.showinfo("Changes Saved", "Changes have been saved successfully.")
            window_edit.destroy()
            load_data()

        button_save = customtkinter.CButton(window_edit, text="Save Changes", )
        button_save.pack(pady=10)

    else:
        messagebox.showerror("Error", "Please select a record to edit.")

def search_data():
    search_query = entry_search.get_text()

    if search_query:
        listbox_data.clear()
        with open('student_courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if search_query in row:
                    listbox_data.insert(row)
    else:
        messagebox.showerror("Error", "Please enter a search query.")





load_data()

app.mainloop()
