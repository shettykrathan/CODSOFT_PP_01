
import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
DATA_FILE = "tasks.json"

# Function to load saved tasks from file
def fetch_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Function to save current tasks into the file
def store_tasks():
    items = []
    for i in range(task_list.size()):
        items.append(task_list.get(i))
    with open(DATA_FILE, "w") as f:
        json.dump(items, f)

# Add new task from entry field
def add_new_task():
    task_text = task_input.get()
    if task_text.strip() != "":
        task_list.insert(tk.END, task_text)
        task_input.delete(0, tk.END)
    else:
        messagebox.showinfo("Empty Task", "Please type something before adding.")

# Delete selected task from listbox
def remove_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showinfo("No Selection", "Choose a task to delete.")

# Load tasks from file into the listbox on startup
def load_on_start():
    tasks = fetch_tasks()
    for t in tasks:
        task_list.insert(tk.END, t)

# UI Setup
root = tk.Tk()
root.title("My Simple To-Do App")
root.geometry("400x400")
root.resizable(False, False)

top_frame = tk.Frame(root)
top_frame.pack(pady=15)

task_input = tk.Entry(top_frame, width=28, font=("Segoe UI", 12))
task_input.pack(side=tk.LEFT, padx=(10, 5))

add_btn = tk.Button(top_frame, text="Add", width=10, command=add_new_task)
add_btn.pack(side=tk.LEFT)

task_list = tk.Listbox(root, width=45, height=15, font=("Segoe UI", 11), selectbackground="gray")
task_list.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

del_btn = tk.Button(btn_frame, text="Delete Task", width=15, command=remove_task)
del_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(btn_frame, text="Save", width=15, command=store_tasks)
save_btn.grid(row=0, column=1, padx=5)

# Populate listbox from saved file
load_on_start()

root.mainloop()
