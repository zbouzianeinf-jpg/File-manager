import tkinter as tk
from tkinter import messagebox
from auth_manager import AuthManager
from file_manager import FileManager

class FileManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Manager")
        self.auth_manager = AuthManager()
        self.file_manager = FileManager()
        self.current_user = None

        self.create_login_register_tabs()

    def create_login_register_tabs(self):
        self.login_frame = tk.Frame(self.master)
        self.register_frame = tk.Frame(self.master)

        for frame in (self.login_frame, self.register_frame):
            frame.grid(row=0, column=0, sticky='nsew')

        self.create_login_tab()
        self.create_register_tab()

    def create_login_tab(self):
        tk.Label(self.login_frame, text="Login").grid(row=0, column=1)
        tk.Label(self.login_frame, text="Username").grid(row=1, column=0)
        tk.Label(self.login_frame, text="Password").grid(row=2, column=0)

        self.username_login = tk.Entry(self.login_frame)
        self.password_login = tk.Entry(self.login_frame, show='*')
        self.username_login.grid(row=1, column=1)
        self.password_login.grid(row=2, column=1)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=3, column=1)

    def create_register_tab(self):
        tk.Label(self.register_frame, text="Register").grid(row=0, column=1)
        tk.Label(self.register_frame, text="Username").grid(row=1, column=0)
        tk.Label(self.register_frame, text="Password").grid(row=2, column=0)

        self.username_register = tk.Entry(self.register_frame)
        self.password_register = tk.Entry(self.register_frame, show='*')
        self.username_register.grid(row=1, column=1)
        self.password_register.grid(row=2, column=1)

        tk.Button(self.register_frame, text="Register", command=self.register).grid(row=3, column=1)

    def login(self):
        username = self.username_login.get()
        password = self.password_login.get()
        self.current_user = self.auth_manager.login(username, password)

        if self.current_user:
            messagebox.showinfo("Login Success", "Welcome, {}!".format(username))
            self.open_user_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def register(self):
        username = self.username_register.get()
        password = self.password_register.get()
        if self.auth_manager.register(username, password):
            messagebox.showinfo("Registration Successful", "You can now login.")
            self.login_frame.tkraise()
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")

    def open_user_dashboard(self):
        user_dashboard = tk.Toplevel(self.master)
        user_dashboard.title("User Dashboard")
        # Add file management functionalities here
        # e.g. self.file_manager.create_file(), etc.

    def open_admin_dashboard(self):
        admin_dashboard = tk.Toplevel(self.master)
        admin_dashboard.title("Admin Dashboard")
        # Admin functionalities here (user management)

if __name__ == '__main__':
    root = tk.Tk()
    app = FileManagerGUI(root)
    root.mainloop()