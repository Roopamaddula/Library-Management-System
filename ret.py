from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable

from sendemailpython import send_email


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("Return")
        self.maxsize(420,280)
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='123456789')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    print("Temp:" + str(temp))
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()

                        self.mycursor.execute("select reserved_stud_id from book where reserved = 'YES' and book_id = %s", [a.get()])
                        temp2 = self.mycursor.fetchone()
                        #print("Temp2" + str(temp2))
                        if temp2:
                            #print("select address from student where stud_id = %s", [temp2[0]])
                            self.mycursor.execute("select address from student where stud_id = %s", [temp2[0]])
                            temp3 = self.mycursor.fetchone()
                            #print(temp3)
                            if temp3:
                                send_email(temp3[0], "Reserved Book is available", "Hi,\n\ Reserved Book is now available. Request you to collect the same from Library.\n\nRegards,\nUEL LMS Group9 ")
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Exception as e:
                    messagebox.showerror("Error",e)
        Label(self, text='Return Book', fg='red',font=('arial', 35, 'bold')).pack()
        Label(self, text='Enter Book ID', font=('Comic Scan Ms', 15, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=a, width=40).place(x=165, y=124)
        Button(self, text="Return", width=25, command=qui).place(x=180, y=180)
ret().mainloop()
