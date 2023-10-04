print("سلام خوش اومدید")
#import
from tkinter import *
import subprocess
from tkinter import messagebox
#data
p = True
users = []
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
def sign_up(e):
    b = False
    for item in users:
        if item["user"] == txt_user.get():
            messagebox.showerror("تکرای", "نام کاربری وارد شده تکراری است!")
            b = True
            break
    if b == False:
        if txt_user.get() == "" or txt_email.get() == "" or txt_pass.get() == "" or txt_pass2.get() == "":
            messagebox.showerror("چن تا چیز خالی است", "لطفا تمام بخش ها را کامل کنید")
        elif txt_pass.get() == txt_pass2.get():
            dic = {"user": txt_user.get(), "password": txt_pass.get(), "email": txt_email.get()}
            users.append(dic)
            print(users)
            messagebox.showinfo("موفقیت امیز", "با موفیقیت انجام شد")
            form.destroy()
            python_file_path = "accept.py"
            subprocess.Popen(["python", python_file_path], shell=True)
        else:
            messagebox.showerror("چک کردن گذرواژه ", "گذرواژه ها متفاوت هستند")

def help(e):
    python_file_path = "help.py"
    subprocess.Popen(["python", python_file_path], shell=True)
def login(e):
        form.destroy()
        python_file_path = "login_pesian.py"
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
logo_label.place(x=165, y=30)
#txt
txt_user = Entry(bg="#79AC78", fg="white", width=30)
txt_user.place(x=280, y=220)
txt_email = Entry(bg="#79AC78", fg="white", width=30)
txt_email.place(x=280, y=260)
txt_pass = Entry(bg="#79AC78", fg="white", width=30, show="•")
txt_pass.place(x=280, y=300)
txt_pass2 = Entry(bg="#79AC78", fg="white", width=30, show="•")
txt_pass2.place(x=280, y=340)
#lbl
lbl_user = Label(text=":نام کاربری ", font="IRHoma", fg="black", width=10)
lbl_user.place(x=180, y=205)
lbl_email = Label(text=":ایمیل ", font="IRHoma", fg="black", width=10)
lbl_email.place(x=180, y=245)
lbl_pass = Label(text=":گذرواژه", font="IRHoma", fg="black", width=10)
lbl_pass.place(x=180, y=285)
lbl_pass2 = Label(text=":گذرواژه مجدد ", font="IRHoma", fg="black", width=17)
lbl_pass2.place(x=120, y=325)
#btn_Language
btn_language=Button(text="Persian", font="IRHoma")
btn_language.place(x=260,y=420)
btn_language.bind("<Button-1>", Language)
#btn_go
btn_go=Button(text="قبول کردن", font="IRHoma")
btn_go.place(x=470,y=255)
btn_go.bind("<Button-1>", sign_up)
#btn_help
btn_help=Button(text="کمک", font="IRHoma")
btn_help.place(x=340,y=420)
btn_help.bind("<Button-1>", help)
#btn_signup
btn_signup = Button(text="ورود کردن", width=5, font="IRHoma")
btn_signup.place(x=404, y=420)
btn_signup.bind("<Button-1>", login)



#done
form.mainloop()
