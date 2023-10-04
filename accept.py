from tkinter import *
form = Tk()
form.iconbitmap(r'C:\Users\Admin\PycharmProjects\crud\image\icon.ico')
form.title("Minecraft")
form.geometry("%dx%d+%d+%d"%(790,790,500,100))
form.resizable(False, False)
lbl=Label(text="Loading...")
lbl.place(x=395,y=395)
form.mainloop()
