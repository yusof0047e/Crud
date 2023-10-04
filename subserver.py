print("خوش اومدی")

#import
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess

#def
def activebtn(e):
    if txt_user.get() == "":
        btn_register.configure(state=DISABLED)
    else:
        btn_register.configure(state=NORMAL)
def onclickregister(e):
    try:
        if btn_register.cget("state") == NORMAL:
            dic = {"name": txt_user.get(), "family": txt_gamil.get(), "age": txt_pass.get()}
            if not exsit(dic):
                load()
                register(dic)
                insert(dic)
                txtuservar.set("")
                txtemailvar.set("")
                txtpassvar.set("")
                txt_user.focus_set()
                messagebox.showinfo("Register", "done successfully")
                print("با موفیقیت ثبت نام شد")
            else:
                messagebox.showinfo("rep", "The target person is repetitive!!!")
                print("کاربر تکراریه")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def getselection(e):
    selection = tbl.selection()
    if selection:
        s = tbl.item(selection)["values"]
        if s:
            txtuservar.set(s[0])
            txtemailvar.set(s[1])
            txtpassvar.set(s[2])
def register(value):
    users.append(value)

def exsit(value):
    for item in users:
        if item["name"] == value["name"] and item["family"] == value["family"] and item["age"] == value["age"]:
            return True
    return False

def load():
    clear()
    for item in users:
        insert(item)

def insert(value):
    tbl.insert('', "end", values=[value["name"], value["family"], value["age"]])

def clear():
    for item in tbl.get_children():
        tbl.delete(item)
def onclicksearch(e):
    serch = txt_search.get()
    result = search(serch)
    clear()
    for item in result:
        insert(item)
    print("در حال جست و جو کردن فرد داخل تی اکس تی سرچ")
def search(value):
    resultlist = []
    for item in users:
        if item["name"] == txt_search.get() or item["family"] == txt_search.get() or item["age"] == txt_search:
            resultlist.append(item)
    return resultlist

def delete(value):
    for item in users:
        if item["name"] == value["name"] and item["family"] == value["family"] and item["age"] == value["age"]:
            users.remove(item)
    clear()
    load()

def onclickdelete(e):
    dialog = messagebox.askyesno("WARNING", "Are you sure you want to delete this profile?")
    if dialog:
        selection = tbl.selection()
        if selection:
            selected_item = tbl.item(selection)
            dic = {"name": selected_item["values"][0], "family": selected_item["values"][1], "age": selected_item["values"][2]}
            delete(dic)
            clear()
            print("فرد با موفقیت حذف شد")
def onclickedit(e):
    select = tbl.selection()
    if select:
        select_item = tbl.item(select)
        dic = {"name": select_item["values"][0], "family": select_item["values"][1], "age": select_item["values"][2]}
        index1 = edit(dic)
        p = users[index1]
        tbl.item(select, values=[p["name"], p["family"], p["age"]])
    print("فرد با موفقیت ادیت شد")

def edit(value):
    index = users.index(value)
    updated_value = {"name": txtuservar.get(), "family": txtemailvar.get(), "age": txtpassvar.get()}
    users[index] = updated_value
    return index

def login(e):
            form.destroy()
            python_file_path = "login_english.py"
            subprocess.Popen(["python", python_file_path], shell=True)
            print("به صفحه لاگین رفتید")
def signup(e):
            form.destroy()
            python_file_path = "signup_english.py"
            subprocess.Popen(["python", python_file_path], shell=True)
            print("به صفحه سرچ رفتید")
#form
form = Tk()
form.iconbitmap("")
form.title("Subserver")
form.configure(bg="#79AC78")
form.geometry(("%dx%d+%d+%d") % (600, 680, 400, 10))
form.resizable(False, False)
form.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')
users = []

#logo
logo_image = PhotoImage(file=r'C:\Users\Admin\PycharmProjects\crud\image\1.png')
logo_image = logo_image.zoom(1)
logo_image = logo_image.subsample(2)
logo_label = Label(form, image=logo_image)
logo_label.place(x=210, y=50)

#tbl
column = ("c1", "c2", "c3")
tbl = ttk.Treeview(form, columns=column, show="headings")
tbl.heading(column[0], text="user")
tbl.column(column[0], width=160)
tbl.heading(column[1], text="email")
tbl.column(column[1], width=180)
tbl.heading(column[2], text="password")
tbl.column(column[2], width=160)
tbl.place(x=55, y=450)
tbl.bind("<Button-1>", getselection)
#other
txtuservar= StringVar()
txtemailvar= StringVar()
txtpassvar= StringVar()
txtsearchvar= StringVar()
#txt
txt_user = Entry(form, justify="center", textvariable=txtuservar, bd=5)
txt_user.bind("<KeyRelease>", activebtn)
txt_user.place(x=240, y=165)

txt_gamil = Entry(form, justify="center", textvariable=txtemailvar, bd=5)
txt_gamil.place(x=240, y=195)

txt_pass = Entry(form, justify="center", textvariable=txtpassvar, bd=5)
txt_pass.place(x=240, y=225)

txt_search = Entry(form, justify="center", textvariable=txtsearchvar, bd=5)
txt_search.place(x=240, y=400)

#lbl
lbl_name = Label(form, text="user", bg="#FFC436", fg="#191D88")
lbl_name.place(x=200, y=170)

lbl_family = Label(form, text="email", bg="#FFC436", fg="#191D88")
lbl_family.place(x=190, y=200)

lbl_age = Label(form, text="pass", bg="#FFC436", fg="#191D88")
lbl_age.place(x=200, y=230)

#btn
btn_register = Button(form, text="Register->", bg="#FFC436", fg="#191D88", width=10)
btn_register.place(x=273, y=255)
btn_register.configure(state=DISABLED)
btn_register.bind("<Button-1>",onclickregister)

btn_delete = Button(form, text="Delete", bg="#FFC436", fg="#191D88", width=10)
btn_delete.place(x=190, y=255)
btn_delete.bind("<Button-1>", onclickdelete)

btn_edit = Button(form, text="Edit", bg="#FFC436", fg="#191D88", width=10)
btn_edit.place(x=273, y=288)
btn_edit.bind("<Button-1>", onclickedit)

btn_search = Button(form, text="Search", bg="#FFC436", fg="#191D88", width=10)
btn_search.place(x=150, y=405)
btn_search.bind("<Button-1>", onclicksearch)

btn_login = Button(form, text="login", bg="#FFC436", fg="#191D88", width=10)
btn_login.place(x=190, y=288)
btn_login.bind("<Button-1>", login)

btn_signup = Button(form, text="signup", bg="#FFC436", fg="#191D88", width=10)
btn_signup.place(x=273, y=321)
btn_signup.bind("<Button-1>", signup)

form.mainloop()
