import tkinter as tk
import json
import os

# ====== App Config ======
APP_BG = "#f4f7fa"
HEADER_BG = "#3f51b5"
HEADER_FG = "white"
BTN_ADD = "#4caf50"
BTN_DONE = "#2196f3"
BTN_DEL = "#f44336"
LIST_BG = "#ffffff"

TASK_FILE = "tasks.json"

# ====== Load/Save Functions ======
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "🕒"
        listbox.insert(tk.END, f"{status} {task['title']}")


def update_toggle_button_text():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        if tasks[index]["done"]:
            btn_toggle.config(text="↩️ Mark as Undone")
        else:
            btn_toggle.config(text="✅ Mark as Done")
    else:
        btn_toggle.config(text="✅ Mark as Done")

# ====== Action Handlers ======
def add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        refresh_listbox()
        entry.delete(0, tk.END)

def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
        refresh_listbox()
        update_toggle_button_text()

def mark_undone():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = False
        save_tasks(tasks)
        refresh_listbox()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        save_tasks(tasks)
        refresh_listbox()
        update_toggle_button_text()

# ====== UI Setup ======
root = tk.Tk()
root.title("📋 Devraj's To-Do App")
root.geometry("500x500")
root.configure(bg=APP_BG)

# ----- Header -----
header = tk.Frame(root, bg=HEADER_BG, height=60)
header.pack(fill="x")

tk.Label(
    header, text="Devraj's To-Do App", font=("Segoe UI", 18, "bold"),
    fg=HEADER_FG, bg=HEADER_BG
).pack(pady=10)

# ----- Entry & Add Button -----
input_frame = tk.Frame(root, bg=APP_BG)
input_frame.pack(pady=20)

entry = tk.Entry(input_frame, font=("Segoe UI", 12), bg="#ffffff", fg="#333", relief="flat", bd=2, insertbackground="#333")
entry.grid(row=0, column=0, padx=10)

btn_add = tk.Button(
    input_frame,
    text="➕ Add Task",
    font=("Segoe UI", 10, "bold"),
    bg=BTN_ADD,
    fg="white",
    padx=12,
    pady=6,
    relief="flat",
    activebackground="#45a049",   # hover color
    cursor="hand2",
    command=add_task
)

btn_add.grid(row=0, column=1)

# ----- Task List -----
listbox = tk.Listbox(
    root,
    font=("Segoe UI", 12),
    bg="#ffffff",
    fg="#222",
    selectbackground="#e3f2fd",   # Light blue
    selectforeground="#000",      # Black text on selection
    relief="flat",
    borderwidth=2,
    highlightthickness=0,
    activestyle="none",
    width=80,
    height=20
)
listbox.bind("<<ListboxSelect>>", lambda e: update_toggle_button_text())
listbox.pack(pady=10)

# ----- Buttons -----
btn_frame = tk.Frame(root, bg=APP_BG)
btn_frame.pack(pady=10)

btn_toggle = tk.Button(
    btn_frame,
    text="✅ Mark as Done",
    font=("Segoe UI", 10, "bold"),
    bg=BTN_DONE,
    fg="white",
    padx=10,
    pady=5,
    command=mark_done
)
btn_toggle.grid(row=0, column=0, padx=10)


tk.Button(
    btn_frame, text="🗑️ Delete", font=("Segoe UI", 10, "bold"),
    bg=BTN_DEL, fg="white", padx=10, pady=5, command=delete_task
).grid(row=0, column=1, padx=10)

# ----- Footer -----
footer = tk.Label(root, text="Built with ❤️ by Devraj", font=("Arial", 9), bg=APP_BG, fg="#999")
footer.pack(pady=20)

# ====== App Start ======
tasks = load_tasks()
refresh_listbox()
root.mainloop()
