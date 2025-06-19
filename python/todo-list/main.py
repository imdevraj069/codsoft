import tkinter as tk
from tkinter import PhotoImage, messagebox
from controllers.user_controller import create_user, login_user
from controllers.task_controller import get_tasks, add_task, toggle_task, delete_task
import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# === CONFIG ===
BG = "#0F0113"
FG = "#ffffff"
INPUT_BG = "#161b22"
ACCENT = "#EF4444"
FONT = ("Microsoft YaHei UI Light", 11)

current_user = None

# === Load User Tasks ===
tasks = []

def load_user_tasks(user):
    global tasks
    tasks = get_tasks(user)
    refresh_task_list()

def add_task_gui():
    title = task_entry.get().strip()
    if not title: return
    add_task(current_user, title)
    task_entry.delete(0, tk.END)
    load_user_tasks(current_user)

def toggle_task_gui():
    selected = task_listbox.curselection()
    if selected:
        toggle_task(current_user, selected[0])
        load_user_tasks(current_user)

def delete_task_gui():
    selected = task_listbox.curselection()
    if selected:
        delete_task(current_user, selected[0])
        load_user_tasks(current_user)

# === REFRESH TASKS ===
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "🕒"
        task_listbox.insert(tk.END, f"{i+1}. {status} {task['title']}")

def add_placeholder(entry, placeholder, color='grey'):
    entry.insert(0, placeholder)
    entry.config(fg=color)

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='white')  # or your normal color

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg=color)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# === ROOT ===
root = tk.Tk()
root.title('todo-app')
root.geometry('925x500+300+200')
root.configure(bg=BG)
root.resizable(False, False)

# === Background Image ===
img = PhotoImage(file=resource_path("images/login.png"))
tk.Label(root, image=img, bg="black").place(x=50, y=50)

# === Pages as Frames ===
frames = {}

def show_frame(name):
    for frame in frames.values():
        frame.place_forget()
    if name == "home":
        frames[name].place(x=0, y=0, relwidth=1, relheight=1)  # Fullscreen
    else:
        frames[name].place(x=480, y=70)

# === Signin Page ===
signin_frame = tk.Frame(root, width=350, height=350, bg="black")
frames["signin"] = signin_frame

tk.Label(signin_frame, text='Sign In', fg='white', bg="black",
         font=('Microsoft YaHei UI Light', 23, "bold")).place(x=100, y=5)

username_entry = tk.Entry(signin_frame, width=25, fg="white", bg="black", insertbackground="white",
                          border=0, font=('Microsoft YaHei UI Light', 13, "bold"))
username_entry.place(x=30, y=80)
add_placeholder(username_entry, "Username")
tk.Frame(signin_frame, width=295, height=2, bg="white").place(x=25, y=107)

password_entry = tk.Entry(signin_frame, width=25, fg="white", bg="black", insertbackground="white",
                          border=0, font=('Microsoft YaHei UI Light', 13, "bold"), show="*")
password_entry.place(x=30, y=140)
add_placeholder( password_entry, "Password")
tk.Frame(signin_frame, width=295, height=2, bg="white").place(x=25, y=167)

def login_action():
    global current_user
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if not username or not password:
        messagebox.showwarning("Error", "Username and password required")
        return
    result = login_user(username, password)
    messagebox.showinfo("Login", result["message"])
    if result["success"]:
        current_user = result["user"]
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        show_frame("home")
        load_user_tasks(current_user)

tk.Button(signin_frame, text="Login", width=25, pady=7, bg=ACCENT, fg="white",
          font=FONT, border=0, command=login_action).place(x=25, y=200)

tk.Button(signin_frame, text="Don't have an account? Sign Up", bg="black", fg=ACCENT,
          font=('Microsoft YaHei UI Light', 9), border=0, command=lambda: show_frame("signup")).place(x=70, y=250)

# === Signup Page ===
signup_frame = tk.Frame(root, width=350, height=350, bg="black")
frames["signup"] = signup_frame

tk.Label(signup_frame, text='Sign Up', fg='white', bg="black",
         font=('Microsoft YaHei UI Light', 23, "bold")).place(x=100, y=5)

signup_user = tk.Entry(signup_frame, width=25, fg="white", bg="black", insertbackground="white",
                       border=0, font=('Microsoft YaHei UI Light', 13, "bold"))
signup_user.place(x=30, y=80)
add_placeholder( signup_user, "Username")
tk.Frame(signup_frame, width=295, height=2, bg="white").place(x=25, y=107)

signup_pass = tk.Entry(signup_frame, width=25, fg="white", bg="black", insertbackground="white",
                       border=0, font=('Microsoft YaHei UI Light', 13, "bold"), show="*")
signup_pass.place(x=30, y=140)
add_placeholder(signup_pass, "Password")
tk.Frame(signup_frame, width=295, height=2, bg="white").place(x=25, y=167)

def register_action():
    username = signup_user.get().strip()
    password = signup_pass.get().strip()
    if not username or not password:
        messagebox.showwarning("Error", "Username and password required")
        return
    result = create_user(username, password)
    messagebox.showinfo("Sign Up", result["message"])
    if result["success"]:
        signup_user.delete(0, tk.END)
        signup_pass.delete(0, tk.END)
        show_frame("signin")

tk.Button(signup_frame, text="Register", width=25, pady=7, bg=ACCENT, fg="white",
          font=FONT, border=0, command=register_action).place(x=25, y=200)

tk.Button(signup_frame, text="Already have an account? Sign In", bg="black", fg=ACCENT,
          font=('Microsoft YaHei UI Light', 9), border=0, command=lambda: show_frame("signin")).place(x=70, y=250)

# === Home Page ===
todo_frame = tk.Frame(root, bg="black")
frames["home"] = todo_frame

tk.Label(todo_frame, text="Welcome, Task Master 👋", font=("Segoe UI", 16, "bold"), bg=BG, fg=FG).pack(pady=10)

task_entry = tk.Entry(todo_frame, width=40, font=FONT, fg=FG, bg=INPUT_BG,
                      insertbackground=FG, relief="flat")
task_entry.pack(pady=(0, 10))

btn_frame = tk.Frame(todo_frame, bg=BG)
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, text="➕ Add", width=10, font=FONT, bg=ACCENT, fg="white", relief="flat", command=add_task_gui)
btn_add.grid(row=0, column=0, padx=5)

btn_toggle = tk.Button(btn_frame, text="✔️ Done/Undone", width=15, font=FONT, bg=ACCENT, fg="white", relief="flat", command=toggle_task_gui)
btn_toggle.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(btn_frame, text="🗑️ Delete", width=10, font=FONT, bg=ACCENT, fg="white", relief="flat", command=delete_task_gui)
btn_delete.grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(todo_frame, width=70, height=12, font=FONT, bg=INPUT_BG,
                          fg=FG, selectbackground="#333", relief="flat")
task_listbox.pack(pady=20)

# === Show initial frame ===
show_frame("signin")

root.mainloop()
