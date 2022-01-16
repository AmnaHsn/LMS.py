
import mysql.connector
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter



#  database connection
connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="library management system")
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()

database_connection = mysql.connector.connect(
   host="localhost",
   port=3306,
   user="root",
   password="",
   database="library management system"
)

print(database_connection)





class LibraryManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ===================================variable=================================================
        self.Member_var = StringVar()
        self.First_name_var = StringVar()
        self.Last_name_var = StringVar()
        self.ID_no_var = StringVar()
        self.Password_var = StringVar()
        self.Book_name_var = StringVar()
        self.Book_ID_var = StringVar()
        self.Author_var = StringVar()
        self.Classification_var = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1543, height=400)
        # ==================================DateFrameLeft========================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="black", bd=12,
                                   relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft,  bg="powder blue", text="Member Type",
                          font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 15, "bold"), textvariable=self.Member_var,
                                 width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblFirst_Name = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("times new roman", 15, "bold"),
                              padx=2, pady=6)
        lblFirst_Name.grid(row=1, column=0, sticky=W)
        txtFirst_Name = Entry(DataFrameLeft, textvariable=self.First_name_var, font=("times new roman", 15, "bold"),
                              width=29)
        txtFirst_Name.grid(row=1, column=1)

        lblLast_Name = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("times new roman", 15, "bold"),
                             padx=2, pady=6)
        lblLast_Name.grid(row=2, column=0, sticky=W)
        txtLast_Name = Entry(DataFrameLeft, textvariable=self.Last_name_var, font=("times new roman", 15, "bold"),
                             width=29)
        txtLast_Name.grid(row=2, column=1)

        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID No", font=("times new roman", 15, "bold"), padx=2,
                         pady=6)
        lblID_No.grid(row=3, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft, textvariable=self.ID_no_var, font=("times new roman", 15, "bold"), width=29)
        txtID_No.grid(row=3, column=1)

        lblPassword = Label(DataFrameLeft, bg="powder blue", text="Password", font=("times new roman", 15, "bold"),
                            padx=2, pady=6)
        lblPassword.grid(row=4, column=0, sticky=W)
        txtPassword = Entry(DataFrameLeft, textvariable=self.Password_var, font=("times new roman", 15, "bold"),
                            width=29)
        txtPassword.grid(row=4, column=1)

        lblBook_Name = Label(DataFrameLeft, bg="powder blue", text="Book Name", font=("times new roman", 15, "bold"),
                             padx=2, pady=6)
        lblBook_Name.grid(row=5, column=0, sticky=W)
        txtBook_Name = Entry(DataFrameLeft, textvariable=self.Book_name_var, font=("times new roman", 15, "bold"),
                             width=29)
        txtBook_Name.grid(row=5, column=1)

        lblBook_ID = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("times new roman", 15, "bold"),
                           padx=2, pady=6)
        lblBook_ID.grid(row=6, column=0, sticky=W)
        txtBook_ID = Entry(DataFrameLeft, textvariable=self.Book_ID_var, font=("times new roman", 15, "bold"), width=29)
        txtBook_ID.grid(row=6, column=1)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author", font=("times new roman", 15, "bold"), padx=2,
                          pady=6)
        lblAuthor.grid(row=7, column=0, sticky=W)
        txtAuthor = Entry(DataFrameLeft, textvariable=self.Author_var, font=("times new roman", 15, "bold"), width=29)
        txtAuthor.grid(row=7, column=1)

        lblClassification = Label(DataFrameLeft, bg="powder blue", text="Classification",
                                  font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblClassification.grid(row=0, column=2, sticky=W)
        txtClassification = Entry(DataFrameLeft, textvariable=self.Classification_var,
                                  font=("times new roman", 15, "bold"), width=29)
        txtClassification.grid(row=0, column=3)

        # ===============================DataFrameRight========================================

        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="black", bd=12, relief=RIDGE,
                                    font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listBooks = ['Matilda', 'Treasure Chest', 'Black House', 'The Twits', 'Billionare Boy']


        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)

        listBox.grid(row=0, column=0, padx=4)

        for item in listBooks:
            listBox.insert(END, item)



        # ============================Buttons Frame======================================


        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1543, height=70)

        btnAddData = Button(Framebutton, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white", command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton,text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command= self.show_data)
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white",command=self.update)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.delete)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white",command=self.reset)
        btnReset.grid(row=0, column=4)

        btnExit = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white", command=self.exit)
        btnExit.grid(row=0, column=5)

        # ============================Information Frame======================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1543, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=(
       "Member Type","FirstName", "LastName", "IDNo", "Password", "BookName", "BookID", "Author", "Classification"),
        xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type", text="Member Type")
        self.library_table.heading("FirstName", text="First Name")
        self.library_table.heading("LastName", text="Last Name")
        self.library_table.heading("IDNo", text="ID No")
        self.library_table.heading("Password", text="Password")
        self.library_table.heading("BookName", text="Book Name")
        self.library_table.heading("BookID", text="Book ID")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Classification", text="Classification")


        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member Type", width=100)
        self.library_table.column("FirstName", width=100)
        self.library_table.column("LastName", width=100)
        self.library_table.column("IDNo", width=100)
        self.library_table.column("Password", width=100)
        self.library_table.column("BookName", width=100)
        self.library_table.column("BookID", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Classification", width=100)


        self.fatch_data()

        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", port=3306, password="",
                                       database="library management system")
        cursor = conn.cursor()
        cursor.execute("insert into student(First_name, Last_name, Student_ID, Student_password, Book_name, Book_ID, Author_name, Classification,Member_Type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.First_name_var.get(),
            self.Last_name_var.get(),
            self.ID_no_var.get(),
            self.Password_var.get(),
            self.Book_name_var.get(),
            self.Book_ID_var.get(),
            self.Author_var.get(),
            self.Classification_var.get(),
            self.Member_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success", "Member has been inserted successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="library management system")
        my_cursor = conn.cursor()
        my_cursor.execute("update student set Member_Type='"+self.Member_var.get()+"',First_name='"+self.First_name_var.get()+"',Last_name='"+self.Last_name_var.get()+"', Student_password='"+self.Password_var.get()+"', Book_name='"+self.Book_name_var.get()+"',Book_ID='"+self.Book_ID_var.get()+"', Author_name='"+self.Author_var.get()+"', Classification='"+self.Classification_var.get()+"' where Student_ID='"+self.ID_no_var.get()+"'")


        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")






    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database= "library management system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.Member_var.set(row[0]),
        self.First_name_var.set(row[1]),
        self.Last_name_var.set(row[2]),
        self.ID_no_var.set(row[3]),
        self.Password_var.set(row[4]),
        self.Book_name_var.set(row[5]),
        self.Book_ID_var.set(row[6]),
        self.Author_var.set(row[7]),
        self.Classification_var.set(row[8])

    def show_data(self):
        self.txtBox.insert(END,"Member Type=\t\t"+ self.Member_var.get() + "\n")
        self.txtBox.insert(END, "First name=\t\t" + self.First_name_var.get() + "\n")
        self.txtBox.insert(END, "Last name=\t\t" + self.Last_name_var.get() + "\n")
        self.txtBox.insert(END, "Student ID=\t\t" + self.ID_no_var.get() + "\n")
        self.txtBox.insert(END, "Student Password=\t\t" + self.Password_var.get() + "\n")
        self.txtBox.insert(END, "Book name=\t\t" + self.Book_name_var.get() + "\n")
        self.txtBox.insert(END, "Book ID=\t\t" + self.Book_ID_var.get() + "\n")
        self.txtBox.insert(END, "Author=\t\t" + self.Author_var.get() + "\n")
        self.txtBox.insert(END, "Classification=\t\t" + self.Classification_var.get() + "\n")

    def reset(self):
        self.Member_var.set(""),
        self.First_name_var.set(""),
        self.Last_name_var.set(""),
        self.ID_no_var.set(""),
        self.Password_var.set(""),
        self.Book_name_var.set(""),
        self.Book_ID_var.set(""),
        self.Author_var.set(""),
        self.Classification_var.set("")
        self.txtBox.delete("1.0",END)

    def exit(self):
        exit=tkinter.messagebox.askyesno("library management system", "Do you want to exit")
        if exit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.ID_no_var.get()=="" or self.Book_ID_var.get()=="":
            messagebox.showerror("Error", "First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="library management system")
            my_cursor = conn.cursor()
            query="delete from student where Student_ID=%s"
            value=(self.ID_no_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted")



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
