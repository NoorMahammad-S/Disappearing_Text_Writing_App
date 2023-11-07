import tkinter as tk
from tkinter import messagebox
import time

# Define the application window
app = tk.Tk()
app.title("Disappearing Text Writing App")
app.geometry("800x600")

# Text widget to type
text_widget = tk.Text(app, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Function to delete text when idle
def delete_text():
    text = text_widget.get("1.0", "end-1c")
    if len(text) == len(delete_text.last_text):
        text_widget.delete("1.0", "end")
    delete_text.last_text = text
    app.after(5000, delete_text)  # Check every 5 seconds

delete_text.last_text = ""  # Variable to keep track of the last text

# Start the initial deletion check
app.after(5000, delete_text)

# Save text to a file
def save_text():
    text = text_widget.get("1.0", "end-1c")
    with open("saved_text.txt", "w") as file:
        file.write(text)

# Load text from a file
def load_text():
    try:
        with open("saved_text.txt", "r") as file:
            text = file.read()
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", text)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No saved text found.")

# Confirm before deleting text
def confirm_delete():
    if messagebox.askyesno("Delete Text", "Are you sure you want to delete all text?"):
        text_widget.delete("1.0", "end")

# Create a menu
menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_text)
file_menu.add_command(label="Load", command=load_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Delete All", command=confirm_delete)

# Main loop
app.mainloop()
