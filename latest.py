import csv
import tkinter as tk
from tkinter import messagebox

def add_record():
    name = entry_name.get()
    email = entry_email.get()

    if name and email:
        with open('records.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email])
        
        messagebox.showinfo("Record Added", "Record has been added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter both name and email.")

def delete_record():
    selected_index = listbox.curselection()

    if selected_index:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        
        if confirmation:
            with open('records.csv', 'r') as file:
                records = list(csv.reader(file))
            
            del records[selected_index[0]]
            
            with open('records.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)
            
            messagebox.showinfo("Record Deleted", "Record has been deleted successfully.")
            load_records()
    else:
        messagebox.showerror("Error", "Please select a record to delete.")

def edit_record():
    selected_index = listbox.curselection()

    if selected_index:
        name = entry_name.get()
        email = entry_email.get()

        if name and email:
            with open('records.csv', 'r') as file:
                records = list(csv.reader(file))
            
            records[selected_index[0]] = [name, email]
            
            with open('records.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)
            
            messagebox.showinfo("Record Updated", "Record has been updated successfully.")
            clear_entries()
            load_records()
        else:
            messagebox.showerror("Error", "Please enter both name and email.")
    else:
        messagebox.showerror("Error", "Please select a record to edit.")

def load_records():
    listbox.delete(0, tk.END)

    with open('records.csv', 'r') as file:
        records = csv.reader(file)
        for row in records:
            listbox.insert(tk.END, f"Name: {row[0]}, Email: {row[1]}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Record Manager")

frame = tk.Frame(root)
frame.pack(pady=20)

label_name = tk.Label(frame, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_email = tk.Label(frame, text="Email:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1)

button_add = tk.Button(root, text="Add Record", command=add_record)
button_add.pack(pady=10)

button_delete = tk.Button(root, text="Delete Record", command=delete_record)
button_delete.pack(pady=5)

button_edit = tk.Button(root, text="Edit Record", command=edit_record)
button_edit.pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

load_records()

root.mainloop()
