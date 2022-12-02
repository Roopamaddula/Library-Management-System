import sys
from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
py=sys.executable

from tkinter import ttk


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(800, 500)
        self.minsize(800, 500)
        self.configure(bg="lightgray")
        self.title("LIBRARY MANAGEMENT SYSTEM")
        self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM",bg='lightgray', fg='black', font=("courier-new", 24, 'bold'))
        self.label3.pack(pady=10)

        
        # create a notebook
        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)
        
        # create frames
        frame1 = ttk.Frame(notebook, width=500, height=300)
        frame2 = ttk.Frame(notebook, width=500, height=300)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame1, text='Admin')
        notebook.add(frame2, text='Student')


#verifying input
        def chex():
            if len(self.user_text.get()) <= 0:
                messagebox.showinfo("Error", "Please enter valid Username")
            elif len(self.pass_text.get()) <= 0:
                messagebox.showinfo("Error", "Please enter valid password")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='123456789')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admins` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Exception as e:
                    messagebox.showinfo(e)
                    
        def chex1():
            if len(self.user_text1.get()) <= 0:
                messagebox.showinfo("Error", "Please enter valid Username")
            elif len(self.pass_text1.get()) <= 0:
                messagebox.showinfo("Error", "Please enter valid password")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='123456789')
                    cursor = conn.cursor()
                    user = self.user_text1.get()
                    password = self.pass_text1.get()
                    cursor.execute('Select * from `student` where name= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options2.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Exception as e:
                    messagebox.showinfo(e)


        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def check():

                    self.label1 = Label(frame1, text="Admin:"   , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=34, y=50)
                    self.user_text = Entry(frame1, textvariable=self.a, width=45)
                    self.user_text.place(x=200, y=60)
                    self.label2 = Label(frame1, text="Password:"   , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=34, y=100)
                    self.pass_text = Entry(frame1, show='*', textvariable=self.b, width=45)
                    self.pass_text.place(x=200, y=110)
                    self.butt = Button(frame1, text="Login",bg ='white', font=10, width=8, command=chex).place(x=200, y=150)
                    
                    self.label1 = Label(frame2, text="Student:"   , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=34, y=50)
                    self.user_text1 = Entry(frame2, textvariable=self.a, width=45)
                    self.user_text1.place(x=200, y=60)
                    self.label2 = Label(frame2, text="Password:"   , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=34, y=100)
                    self.pass_text1 = Entry(frame2, show='*', textvariable=self.b, width=45)
                    self.pass_text1.place(x=200, y=110)
                    self.butt = Button(frame2, text="Login",bg ='white', font=10, width=8, command=chex1).place(x=200, y=150)
                    self.butt = Button(frame2, text="Register",bg ='white', font=10, width=8, command=a_s).place(x=350, y=150)


        check()

Lib().mainloop()
