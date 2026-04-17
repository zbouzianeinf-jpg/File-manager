import tkinter as tk
from tkinter import filedialog, messagebox

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("600x400")

        self.label = tk.Label(root, text="Welcome to File Manager", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.open_button = tk.Button(root, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Selected File", f"You selected: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()