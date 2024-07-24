import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return
    
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(generated_password)

root = tk.Tk()
root.title("Password Generator")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

length_label = ttk.Label(mainframe, text="Password Length:")
length_label.grid(column=0, row=0, sticky=tk.W)

length_entry = ttk.Entry(mainframe, width=10)
length_entry.grid(column=1, row=0, sticky=tk.W)

lowercase_var = tk.BooleanVar()
lowercase_check = ttk.Checkbutton(mainframe, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(column=0, row=1, sticky=tk.W)

uppercase_var = tk.BooleanVar()
uppercase_check = ttk.Checkbutton(mainframe, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(column=0, row=2, sticky=tk.W)

numbers_var = tk.BooleanVar()
numbers_check = ttk.Checkbutton(mainframe, text="Numbers", variable=numbers_var)
numbers_check.grid(column=0, row=3, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_check = ttk.Checkbutton(mainframe, text="Symbols", variable=symbols_var)
symbols_check.grid(column=0, row=4, sticky=tk.W)

generate_button = ttk.Button(mainframe, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=5, columnspan=2, pady=10)

password_var = tk.StringVar()
password_entry = ttk.Entry(mainframe, textvariable=password_var, width=30, state='readonly')
password_entry.grid(column=0, row=6, columnspan=2, pady=10)

root.mainloop()
