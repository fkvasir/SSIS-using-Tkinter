import csv
import tkinter as tk
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("1080x720")
app.title("SSISv1")

title = customtkinter.CTkLabel(app, text = "Simple Student Information System")
title.pack(padx=10, pady= 10)

# def add_student():
#     name = entry_name.get()
#     id_number = entry_id.get()
#     year_level = entry_year.get()
#     sex = entry_sex.get()
#     courses = listbox_courses.get_selected_items()

#     if name and id_number and year_level and courses:
#         with open('student_info.csv', 'a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow([name, id_number, year_level,sex] + courses)
        
#         messagebox.showinfo("Student Added", "Student has been added successfully.")
#         clear_fields()
#     else:
#         messagebox.showerror("Error", "Please fill in all fields and select at least one course.")

# def search_students():
#     search_query = entry_search.get()

#     if search_query:
#         listbox_students.clear()
#         with open('student_info.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if search_query in row:
#                     listbox_students.insert(row)
#     else:
#         messagebox.showerror("Error", "Please enter a search query.")

# def update_student():
#     selected_data = listbox_students.get_selected_items()

#     if selected_data:
#         selected_name = selected_data[0]
#         selected_id = selected_data[1]
#         selected_year = selected_data[2]
#         selected_courses = selected_data[3:]

#         window_update = customtkinter.CTk()
#         window_update.title("Update Student")

#         frame_update = customtkinter.CTkFrame(window_update)
#         frame_update.pack(pady=20)

#         label_name = customtkinter.CTkLabel(frame_update, text="Name:")
#         label_name.grid(row=0, column=0)
#         entry_name = customtkinter.CTkEntry(frame_update)
#         entry_name.grid(row=0, column=1)
#         entry_name.set_text(selected_name)

#         label_id = customtkinter.CTkLabel(frame_update, text="ID Number:")
#         label_id.grid(row=1, column=0)
#         entry_id = customtkinter.CTkEntry(frame_update)
#         entry_id.grid(row=1, column=1)
#         entry_id.set_text(selected_id)

#         label_year = customtkinter.CTkLabel(frame_update, text="Year Level:")
#         label_year.grid(row=2, column=0)
#         entry_year = customtkinter.CTkEntry(frame_update)
#         entry_year.grid(row=2, column=1)
#         entry_year.set_text(selected_year)

#         label_courses = customtkinter.CTkLabel(frame_update, text="Courses:")
#         label_courses.grid(row=3, column=0)
#         entry_courses = customtkinter.CTkEntry(frame_update)
#         entry_courses.grid(row=3, column=1)
#         entry_courses.set_text(', '.join(selected_courses))

#         def save_changes():
#             new_name = entry_name.get_text()
#             new_id = entry_id.get_text()
#             new_year = entry_year.get_text()
#             new_courses = entry_courses.get_text().split(', ')
#             updated_data = [new_name, new_id, new_year] + new_courses

#             with open('student_info.csv', 'r') as file:
#                 records = list(csv.reader(file))
            
#             with open('student_info.csv', 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 for row in records:
#                     if row != selected_data:
#                         writer.writerow(row)
#                 writer.writerow(updated_data)

#             messagebox.showinfo("Changes Saved", "Changes have been saved successfully.")
#             window_update.destroy()
#             load_students()

#         button_save = customtkinter.CTkButton(window_update, text="Save Changes", command=save_changes)
#         button_save.pack(pady=10)

#     else:
#         messagebox.showerror("Error", "Please select a student to update.")

# def delete_student():
#     selected_data = listbox_students.get_selected_items()

#     if selected_data:
#         confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this student?")
#         if confirmation:
#             with open('student_info.csv', 'r') as file:
#                 records = list(csv.reader(file))
            
#             with open('student_info.csv', 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 for row in records:
#                     if row != selected_data:
#                         writer.writerow(row)
            
#             messagebox.showinfo("Deletion Successful", "Student has been deleted.")
#             load_students()

#     else:
#         messagebox.showerror("Error", "Please select a student to delete.")

# def clear_fields():
#     entry_name.delete(0, tk.END)
#     entry_id.delete(0, tk.END)
#     entry_year.delete(0, tk.END)
#     listbox_courses.clear_selection()

# def load_students():
#     listbox_students.clear()
#     with open('student_info.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             listbox_students.insert(row)

frame_courses = customtkinter.CTkFrame(app)
frame_courses.pack(pady=10)

label_courses = customtkinter.CTkLabel(frame_courses, text="Courses:")
label_courses.pack(pady=10)

courses = customtkinter.CTkFrame(frame_courses)
courses.pack(pady=10)

frame_student = customtkinter.CTkFrame(app)
frame_student.pack(pady=20)

label_name = customtkinter.CTkLabel(frame_student, text="Name:")
label_name.grid(row=0, column=0)
entry_name = customtkinter.CTkEntry(frame_student)
entry_name.grid(row=0, column=1)

label_id = customtkinter.CTkLabel(frame_student, text="ID Number:")
label_id.grid(row=1, column=0)
entry_id = customtkinter.CTkEntry(frame_student)
entry_id.grid(row=1, column=1)

label_year = customtkinter.CTkLabel(frame_student, text="Year Level:")
label_year.grid(row=2, column=0)
entry_year = customtkinter.CTkEntry(frame_student)
entry_year.grid(row=2, column=1)


# listbox_courses = customtkinter.CListBox(frame_courses, width=50)
# listbox_courses.pack(pady=5)

frame_buttons = customtkinter.CTkFrame(app)
frame_buttons.pack(pady=10)

button_add_student = customtkinter.CTkButton(frame_buttons, text="Add Student")
button_add_student.grid(row=0, column=0, padx=5)

button_search_students = customtkinter.CTkButton(frame_buttons, text="Search Students")
button_search_students.grid(row=0, column=1, padx=5)

button_update_student = customtkinter.CTkButton(frame_buttons, text="Update Student")
button_update_student.grid(row=0, column=2, padx=5)

button_delete_student = customtkinter.CTkButton(frame_buttons, text="Delete Student")
button_delete_student.grid(row=0, column=3, padx=5)

frame_search = customtkinter.CTkFrame(app)
frame_search.pack(pady=20)

label_search = customtkinter.CTkLabel(frame_search, text="Search:")
label_search.grid(row=0, column=0)
entry_search = customtkinter.CTkEntry(frame_search)
entry_search.grid(row=0, column=1)

button_clear_fields = customtkinter.CTkButton(app, text="Clear Fields")
button_clear_fields.pack(pady=10)

frame_students = customtkinter.CTkFrame(app)
frame_students.pack(pady=20)

label_students = customtkinter.CTkLabel(frame_students, text="Students:")
label_students.pack()

listbox_students = customtkinter.CTkFrame(frame_students)
listbox_students.pack(pady=20)

# load_students()

app.mainloop()
