#import
from tkinter import *
import subprocess
from tkinter import messagebox
#def
def passyad():
    print("به صفحه فرستادن کد منتقل شد.")
    python_file_path = "passyad.py"
    subprocess.Popen(["python", python_file_path], shell=True)
def Language(e):
    print("فارسی شد.")
    form.destroy()
    python_file_path = "login_pesian.py"
    subprocess.Popen(["python", python_file_path], shell=True)
def Accept(e):
    username = txt_user.get()
    password = txt_pass.get()
    if not username or not password:
        messagebox.showerror("warning", "Please enter the correct password or email.")
        print("پسورد یا نام کاربری نامعتبر ثبت شده.")
    else:
        print("روی ثبت کردن کلیک شد.")
        messagebox.showinfo("nice","After successful registration, you will be taken to the login page")
        form.destroy()
        python_file_path = "accept.py"
        subprocess.Popen(["python", python_file_path], shell=True)
def help(e):
    python_file_path = "help.py"
    subprocess.Popen(["python", python_file_path], shell=True)
def login(e):
    form.destroy()
    python_file_path = "signup_english.py"
    subprocess.Popen(["python", python_file_path], shell=True)
def subserver(e):
    form.destroy()
    python_file_path = "subserver_login.py"
    subprocess.Popen(["python", python_file_path], shell=True)

#form
form = Tk()
form.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')
form.title("Minecraft")
form.geometry("700x600+400+10")
form.resizable(False, False)
#logo
logo_image = PhotoImage(file=r'C:\Users\Admin\PycharmProjects\crud\image\1.png')
logo_image = logo_image.zoom(2)
logo_image = logo_image.subsample(2)
logo_label = Label(form, image=logo_image)
logo_label.place(x=165, y=80)
#txt
txt_user = Entry(bg="#79AC78", fg="white", width=30)
txt_user.place(x=280, y=260)
txt_pass = Entry(bg="#79AC78", fg="white", width=30, show="•")
txt_pass.place(x=280, y=300)
#lbl
lbl_user = Label(text="Email: ", font="IRHoma", fg="black", width=10)
lbl_user.place(x=180, y=245)
lbl_pass = Label(text="Password: ", font="IRHoma", fg="black", width=10)
lbl_pass.place(x=180, y=285)
#link
lbl_passyad = Label(text="Forgot your password?", font="IRHoma", fg="#79AC78", cursor="hand2")
lbl_passyad.place(x=250, y=330)
lbl_passyad.bind("<Button-1>", lambda event: passyad())
#btn_Language
btn_language=Button(text="Persian", font="IRHoma")
btn_language.place(x=260,y=370)
btn_language.bind("<Button-1>", Language)
#btn_go
btn_go=Button(text="Accept", font="IRHoma")
btn_go.place(x=470,y=255)
btn_go.bind("<Button-1>", Accept)
#btn_help
btn_help=Button(text="Help", font="IRHoma")
btn_help.place(x=340,y=370)
btn_help.bind("<Button-1>", help)
#btn_signup
btn_signup = Button(text="Signup", width=5, font="IRHoma")
btn_signup.place(x=404, y=370)
btn_signup.bind("<Button-1>", login)
#btn_subserver
btn_subserever = Button(text="Subserver1", width=10, font="IRHoma")
btn_subserever.place(x=600, y=500)
btn_subserever.bind("<Button-1>", subserver)

form.mainloop()
