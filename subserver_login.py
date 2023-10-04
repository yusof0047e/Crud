from tkinter import *
from tkinter import messagebox
import subprocess

global_password = "0526136"

def login():
    user_password = txt.get()
    if user_password == global_password:
        messagebox.showinfo("That's true", "That's true")
        form.destroy()
        python_file_path = "subserver.py"
        subprocess.Popen(["python", python_file_path], shell=True)
    else:
        messagebox.showerror("It was a mistake", "It was a mistake")
        form.destroy()

form = Tk()
form.iconbitmap("")
form.title("Subserver")
form.configure(bg="#79AC78")
form.geometry(("%dx%d+%d+%d") % (300, 150, 400, 10))
form.resizable(False, False)
form.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')

lbl = Label(text="Enter the subserver password.")
lbl.place(x=50, y=30)
txt = Entry(form, justify="center", bd=5)
txt.place(x=50, y=60)
btn = Button(text="login", command=login)
btn.place(x=50, y=90)

form.mainloop()
