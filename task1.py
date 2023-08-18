

import tkinter as tk
from tkinter import messagebox

def add_task():
    task_text = entry_task.get()
    if task_text:
        listbox_tasks.insert(tk.END, task_text)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_selected_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_selected_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        new_task_text = entry_task.get()
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(selected_index, new_task_text)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")
    finally:
        entry_task.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Application")

entry_task = tk.Entry(root, font=("Helvetica", 14), width=30)
entry_task.pack(pady=10, padx=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_add_task = tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=add_task)
button_add_task.pack(side=tk.LEFT, padx=5)

button_update_task = tk.Button(button_frame, text="Update Task", font=("Arial", 12), command=update_selected_task)
button_update_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), command=delete_selected_task)
button_delete_task.pack(side=tk.LEFT, padx=5)

listbox_tasks = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox_tasks.pack(pady=20)

root.mainloop()




