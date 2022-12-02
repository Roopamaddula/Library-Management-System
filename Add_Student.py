from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Reister Student')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        n = StringVar()
        p = StringVar()
        a = StringVar()
        t = StringVar()
#verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            elif len(t.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Password")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='123456789')
                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    pwd = t.get()
                    self.myCursor.execute("Insert into student(name,phone_number,address,password) values (%s,%s,%s,%s)",[name1,pn1,add1,pwd])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Student Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Name:',bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=n, width=30).place(x=200, y=84)
        Label(self, text='Password:',bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=t, width=30).place(x=200, y=132)
        Label(self, text='Phone Number:',bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Label(self, text='Email:',bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=230)
        Entry(self, textvariable=a, width=30).place(x=200, y=232)
        Button(self, text="Submit",width = 15,command=asi).place(x=230, y=270)

Add().mainloop()
