import tkinter as tk
from tkinter import messagebox

class CrackMeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CrackMe")
        self.root.geometry("400x300")
        self.root.config(bg="#34495e")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Welcome to CrackMe", font=("Helvetica", 18, "bold"), fg="#ecf0f1", bg="#34495e")
        title_label.pack(pady=30)

        self.password_label = tk.Label(self.root, text="Enter Password", font=("Helvetica", 12), fg="#ecf0f1", bg="#34495e")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 12), width=25, bd=0, relief="flat", show="*", fg="#2c3e50", bg="#ecf0f1")
        self.password_entry.pack(pady=5)

        self.attempts_label = tk.Label(self.root, text="Attempts Left: 3", font=("Helvetica", 10), fg="#ecf0f1", bg="#34495e")
        self.attempts_label.pack(pady=10)

        crack_button = tk.Button(self.root, text="Enter!", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#e74c3c", width=12, relief="flat", command=self.crack)
        crack_button.pack(pady=20)

        footer_label = tk.Label(self.root, text="CrackMe-Reverse Engineering Practice", font=("Helvetica", 8), fg="#7f8c8d", bg="#34495e")
        footer_label.pack(side="bottom", pady=10)

        self.attempts_left = 3

    def crack(self):
        correct_password = "CRACKIT"
        entered_password = self.password_entry.get()

        if entered_password == correct_password:
            messagebox.showinfo("Success", "Congratulations! You've cracked the password!")
            self.root.quit()
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                messagebox.showerror("Game Over", "You've used all attempts. The app will now close.")
                self.root.quit()
            else:
                self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
                messagebox.showwarning("Incorrect", "Wrong password. Try again!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CrackMeApp(root)
    root.mainloop()
