import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit():
    res = first_entry.get()
    res1 = second_entry.get()
    if (res=="" and res1=="") or (res=="") or (res1==""):
        messagebox.showwarning("Login","Fill up First")
    elif (res!="" and res1!="") or (res!="") or (res1!=""):
        root.destroy()
        root1 = tk.Tk()
        root1.geometry("400x200")

        title1 = ttk.Label(root1, text="Login")
        title1.place(relx=0.43,rely=0.12)
        title1.config(font=("Courier", 14))

        first_label1 = ttk.Label(root1, text="Enter your Username:")
        first_label1.place(relx=0.19, rely=0.29)
        first_entry1 = ttk.Entry(root1)
        first_entry1.place(relx=0.49, rely=0.29)

        second_label1 = ttk.Label(root1, text="Enter your Password:")
        second_label1.place(relx=0.19, rely=0.38)
        second_entry1 = ttk.Entry(root1,show='*')
        second_entry1.place(relx=0.49, rely=0.38)

        def user_login():
            if res == first_entry1.get() and res1==second_entry1.get():
                messagebox.showinfo("Login","Success")
                root1.destroy()
            else:
                messagebox.showerror("Login","Incorrect")
        second_button1 = ttk.Button(root1, text="Login", command = user_login)
        second_button1.place(relx=0.43,rely=0.49)
        root1.mainloop()

root = tk.Tk()
root.title("Savings")
root.geometry("500x400")

title = ttk.Label(root, text ="Register Account")
title.place(relx=0.33,rely=0.12)
title.config(font=("Courier", 14))

first_label = ttk.Label(root, text="Enter your Username:")
first_label.place(relx=0.23, rely=0.32)
first_entry = ttk.Entry(root)
first_entry.place(relx=0.49,rely=0.32)

second_label = ttk.Label(root, text="Enter your Password:")
second_label.place(relx=0.23, rely=0.38)
second_entry = ttk.Entry(root)
second_entry.place(relx=0.49, rely=0.38)

button = ttk.Button(root, text="Register",command=submit)
button.place(relx=0.42,rely=0.45)
root.mainloop()
