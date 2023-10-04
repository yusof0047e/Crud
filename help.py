from tkinter import *

root=Tk()
root.geometry("%dx%d+%d+%d"%(700,400,500,100))
root.title("Help")
root.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')
root.configure(bg="#116D6E")
lbl=Label(text="English: If you have registered, enter your username and password.",bg="#116D6E",fg="white")
lbl.place(x=10,y=40)

lbl2=Label(text="If you do not have an account, click on the sign up button to register.",bg="#116D6E",fg="white")
lbl2.place(x=10,y=70)

lbl3=Label(text="by yusof mardanzadeh",bg="#116D6E",fg="white")
lbl3.place(x=10,y=130)

lbl4=Label(text="اگر اکانت دارید user name و password را وارد نمایید",bg="#116D6E",fg="white")
lbl4.place(x=10,y=190)

lbl5=Label(text="اگر که اکانت ندارید روی دکمه sign up بزنید و ثبت نام کنید ",bg="#116D6E",fg="white")
lbl5.place(x=10,y=220)

lbl6=Label(text="ساخته شده توسط یوسف مردان زاده :)",bg="#116D6E",fg="white")
lbl6.place(x=10,y=250)

lbl7=Label(text=" فارسی: ",bg="#116D6E",fg="white")
lbl7.place(x=10,y=160)


root.mainloop()
