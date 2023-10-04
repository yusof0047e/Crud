from tkinter import *

win=Tk()
win.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')
win.geometry("%dx%d+%d+%d"%(500,230,500,100))
win.title("Have you forgotten your password?")
lbl_pass=Label(text="We have sent a code to your email, enter it. ",width=50)
lbl_pass.place(x=40,y=30)
txt_pass=Entry(bg="#FFF4F4",fg="black",width=10)
txt_pass.place(x=170,y=70)
btn_signup=Button(text="go ",width=3,font="caveat",bg="#F86F03")
btn_signup.place(x=250,y=67)
btn_signup.bind()
ssss=Button(text="Didn't get the code? ",width=30,font="caveat",bg="#F86F03")
ssss.place(x=120,y=180)
ssss.bind()


win.mainloop()
