import csv
import tkinter as tk
from tkinter import messagebox


def add_record():
    name = entry_name.get()
    course = entry_course.get()
    age = entry_age.get()
    if name and course and age:
        with open("records.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, course, age])

        messagebox.showinfo("Record Added", "Record has been added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter both name and course.")


def delete_record():
    selected_index = listbox.curselection()

    if selected_index:
        confirmation = messagebox.askyesno(
            "Confirm Deletion", "Are you sure you want to delete this record?"
        )

        if confirmation:
            with open("records.csv", "r") as file:
                records = list(csv.reader(file))

            del records[selected_index[0]]

            with open("records.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(records)

            messagebox.showinfo(
                "Record Deleted", "Record has been deleted successfully."
            )
            load_records()
    else:
        messagebox.showerror("Error", "Please select a record to delete.")


def edit_record():
    selected_index = listbox.curselection()

    if selected_index:
        name = entry_name.get()
        course = entry_course.get()
        age = entry_age.get()

        if name and course and age:
            with open("records.csv", "r") as file:
                records = list(csv.reader(file))

            records[selected_index[0]] = [name, course, age]

            with open("records.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(records)

            messagebox.showinfo(
                "Record Updated", "Record has been updated successfully."
            )
            clear_entries()
            load_records()
        else:
            messagebox.showerror("Error", "Please enter both name and course.")
    else:
        messagebox.showerror("Error", "Please select a record to edit.")


def load_records():
    listbox.delete(0, tk.END)

    with open("records.csv", "r") as file:
        records = csv.reader(file)
        for row in records:
            listbox.insert(tk.END, f"Name: {row[0]}, Course: {row[1]}")


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_age.delete(0,tk.END)


root = tk.Tk()
root.title("Student Information System")

frame = tk.Frame(root)
frame.pack(pady=20)

label_name = tk.Label(frame, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_course = tk.Label(frame, text="Course:")
label_course.grid(row=1, column=0)
entry_course = tk.Entry(frame)
entry_course.grid(row=1, column=1)

label_age = tk.Label(frame, text="Age:")
label_age.grid(row= 2,column= 0)
entry_age = tk.Entry(frame)
entry_age.grid(row=2,column=1)

button_add = tk.Button(root, text="Add Record", command=add_record)
button_add.pack(pady=10)

button_delete = tk.Button(root, text="Delete Record", command=delete_record)
button_delete.pack(pady=5)

button_edit = tk.Button(root, text="Edit Record", command=edit_record)
button_edit.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=5)

load_records()

root.mainloop()
