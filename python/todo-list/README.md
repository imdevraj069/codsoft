# 📝 Tkinter ToDo App with Authentication

A clean and simple ToDo desktop application built with **Python + Tkinter**.  
It supports basic user authentication (Sign In / Sign Up) and task management features per user.

> Built by Devraj 🚀

---

## 📸 Preview

![Login Screen](images/auth-screen.jpg)
![Login Screen](images/todo-list-screen.jpg)

---

## ✅ Features

- 👤 User Sign Up & Login
- ✅ Task Management (Add, Toggle Done, Delete)
- 🌓 Dark-themed UI
- 📦 Modular Structure (Controllers for user & task logic)
- 🖼️ Custom background image
- 🔐 Session-based task access per user

---

## 📁 Project Structure
```bash
todo-app/
├── main.py # Main GUI application
├── controllers/
│ ├── user_controller.py # Handles user creation and login
│ └── task_controller.py # Handles task-related logic
├── images/
│ └── login.png # Background image
├── requirements.txt # Dependencies
└── README.md # Project instructions

```
---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

2. Install dependencies
Make sure you have Python 3.7 or higher installed.

```bash
pip install -r requirements.txt
```

3. Run the app
```bash
python main.py
```


## 💡 How It Works

- Launches to the **Sign In** screen.
- Users can **Sign Up** if they don't have an account.
- On login, only that user's tasks are shown.
- Tasks can be added, marked as **done/undone**, and deleted.

> 🗒️ **Note**: Data is currently stored **in memory**. To persist between sessions, consider integrating **SQLite** or **JSON** file storage.

---

## 🔧 Customization Tips

- 🖼️ Change the background image in `images/login.png`.
- 🎨 UI customization is done in `main.py` using **Tkinter**.
- 🧠 Extend `user_controller.py` and `task_controller.py` to use persistent storage like SQLite or JSON.
- 🔐 Add password hashing using `bcrypt` for better security.

---

## 🛠 Packaging for Windows

To convert the app into a standalone `.exe` file:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## 🙋 FAQ
1. Q: Is it cross-platform?
✅ Yes! It works on Windows, macOS, and Linux (requires Python).

2. Q: Where is data stored?
🧠 Currently, it's stored in memory. You can extend it to use a database or file storage.

3. Q: Can I modify the UI?
🎨 Absolutely! It's built in pure Tkinter — just edit main.py.


---

# 📄 License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

# ✍️ Author
>Made with ❤️ by Devraj
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/iamdevraj069/)
[![github](https://img.shields.io/badge/github-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://github.com/imdevraj069)

