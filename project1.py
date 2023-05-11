import csv
import tkinter as tk


class CSVEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Records")

        # input fields
        tk.Label(self.master, text="Name:").grid(row=0, column=0, padx=2, pady=2)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=2, pady=5)

        tk.Label(self.master, text="Course:").grid(row=1, column=0, padx=2, pady=2)
        self.course_entry = tk.Entry(self.master)
        self.course_entry.grid(row=1, column=1, padx=2, pady=5)

        tk.Label(self.master, text="ID no. ").grid(row=0, column=2, padx=2, pady=2)
        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=1, column=2, padx=2, pady=5)

        # buttons
        self.add_button = tk.Button(self.master, text="Add", command=self.add_data)
        self.add_button.grid(row=2, column=0, padx=2, pady=2)

        self.search_button = tk.Button(
            self.master, text="Search", command=self.search_data
        )
        self.search_button.grid(row=2, column=1, padx=2, pady=2)

        self.modify_button = tk.Button(
            self.master, text="Modify", command=self.modify_data
        )
        self.modify_button.grid(row=2, column=2, padx=2, pady=2)

        self.delete_button = tk.Button(
            self.master, text="Delete", command=self.delete_data
        )
        self.delete_button.grid(row=2, column=3, padx=2, pady=2)

        # table to display data
        tk.Label(self.master, text="Data:").grid(row=3, column=0, padx=5, pady=5)
        self.data_table = tk.Text(self.master, height=10, width=50)
        self.data_table.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # load existing data from file
        self.load_data()

    def load_data(self):
        with open("student-records.csv", "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            self.display_data(data)

    def display_data(self, data):
        self.data_table.delete("1.0", tk.END)
        for row in data:
            self.data_table.insert(tk.END, f"{row[0]}, {row[1]}\n")

    def add_data(self):
        name = self.name_entry.get()
        course = self.course_entry.get()
        idno = self.id_entry.get()
        with open("student-records.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, course, idno])
        self.load_data()

    def search_data(self):
        query = self.name_entry.get()
        with open("student-records.csv", "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader if query in row[0]]
            self.display_data(data)

    def modify_data(self):
        with open("student_records.csv", "r") as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
        for row in reader:
            row[1] = row[1].upper()

        writer.writerow(row)

    def delete_data(self):
        query = self.name_entry.get()
        with open("student-records.csv", "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader if query not in row[0]]
        with open("student-records.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        self.load_data()


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVEditor(root)
    root.mainloop()
