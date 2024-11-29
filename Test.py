import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")
app.resizable(False, False)

# Heading
heading = tk.Label(app, text="To-Do List", font=("Helvetica", 16, "bold"))
heading.pack(pady=10)

# Input frame for adding tasks
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 12))
task_entry.grid(row=0, column=0, padx=10)

add_task_btn = tk.Button(input_frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_task_btn.grid(row=0, column=1)

# Task list
task_listbox = tk.Listbox(app, width=45, height=15, font=("Helvetica", 12))
task_listbox.pack(pady=10)

# Action buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

remove_task_btn = tk.Button(button_frame, text="Remove Task", font=("Helvetica", 12), command=remove_task)
remove_task_btn.grid(row=0, column=0, padx=10)

clear_tasks_btn = tk.Button(button_frame, text="Clear All", font=("Helvetica", 12), command=clear_tasks)
clear_tasks_btn.grid(row=0, column=1, padx=10)

# Run the app
app.mainloop()
