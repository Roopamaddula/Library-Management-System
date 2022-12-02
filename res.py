from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable


class res(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("Reserve")
        self.maxsize(600,280)
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.cal = 0
        a = StringVar()
        b = StringVar()

        def reservebook():
            if len(a.get()) == '0' or len(b.get()) == '0':
                messagebox.showerror("Error","Please Enter Correct details")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='123456789')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select availability from book where availability = 'NO' and reserved = 'NO' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set reserved ='YES', reserved_stud_id = %s where book_id = %s", [b.get(), a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        self.mycursor.close()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Reserve Succesfully')
                        d = messagebox.askyesno("Confirm", "Reserve more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'res.py'))
                        else:
                            self.destroy()
							
                    else:
                        messagebox.showinfo("Oop's", "Book already Reserved or Not Applicable")
                except Exception as e:
                    messagebox.showerror("e", e)

        Label(self, text='Reserve Book', bg='gray',font=('arial', 35, 'bold')).pack()

        Label(self, text='Enter Book ID:', bg='gray',font=('Comic Scan Ms', 15, 'bold')).place(x=15, y=120)
        Entry(self, textvariable=a, width=40).place(x=190, y=124)

        Label(self, text='Enter Student ID:', bg='gray',font=('Comic Scan Ms', 15, 'bold')).place(x=15, y=170)
        Entry(self, textvariable=b, width=40).place(x=190, y=170)
        
        Button(self, text="Reserve", width=25, command=reservebook).place(x=190, y=220)
res().mainloop()
