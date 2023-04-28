import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Person GUI")
        self.person = None
        
        # Create label widgets for user input
        name_label = tk.Label(master, text="Name: ")
        name_label.grid(row=0, column=0)
        age_label = tk.Label(master, text="Age: ")
        age_label.grid(row=1, column=0)
        
        # Create entry widgets for user input
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=1, column=1)
        
        # Create buttons for user actions
        create_button = tk.Button(master, text="Create Person", command=self.create_person)
        create_button.grid(row=2, column=0, columnspan=2, pady=10)
        show_button = tk.Button(master, text="Show Person", command=self.show_person)
        show_button.grid(row=3, column=0, columnspan=2, pady=10)
        clear_button = tk.Button(master, text="Clear Entries", command=self.clear_entries)
        clear_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def create_person(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        if name == "" or age == "":
            messagebox.showerror("Error", "Please enter both a name and age")
            return
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer age")
            return
        self.person = Person(name, age)
        messagebox.showinfo("Success", "Person created successfully!")
        
    def show_person(self):
        if self.person is None:
            messagebox.showerror("Error", "No person has been created yet")
            return
        messagebox.showinfo("Person Info", str(self.person))
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

root = tk.Tk()
app = App(root)
root.mainloop()

