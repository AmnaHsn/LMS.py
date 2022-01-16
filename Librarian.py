from tkinter import*
from tkinter import ttk

class Librarian:
    def __init__(self,root):
        self.root=root
        self.root.title("Librarian")
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="LIBRARIAN", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1543, height=400)



        lblBook_type = Label(frame, bg="powder blue", text="Book Type", font=("times new roman", 15, "bold"),padx=50,pady=24)
        lblBook_type.grid(row=1, column=0, sticky=W)

        comBook_records = ttk.Combobox(frame, font=("times new roman", 15, "bold"),width=27, state="readonly")
        comBook_records["value"] = ("English", "Urdu", "Biology","Physics","Geography","Maths","Novels")
        comBook_records.grid(row=1, column=1)

        lblBooks_issue = Label(frame, bg="powder blue", text="Books issue", font=("times new roman", 15, "bold"), padx=50,pady=24)
        lblBooks_issue.grid(row=2, column=0, sticky=W)
        txtBooks_issue = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        txtBooks_issue.grid(row=2, column=1)

        lblNo_of_books = Label(frame, bg="powder blue", text="No of books", font=("times new roman", 15, "bold"), padx=50, pady=24)
        lblNo_of_books.grid(row=3, column=0, sticky=W)
        txtNo_of_books = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        txtNo_of_books.grid(row=3, column=1)

        lblNo_of_availablebooks = Label(frame, bg="powder blue", text="No of Available books", font=("times new roman", 15, "bold"), padx=50, pady=24)
        lblNo_of_availablebooks.grid(row=4, column=0, sticky=W)
        txtNo_of_availablebooks = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        txtNo_of_availablebooks.grid(row=4, column=1)

        lblNo_of_returningbooks = Label(frame, bg="powder blue", text="No of Returning books", font=("times new roman", 15, "bold"), padx=50, pady=24)
        lblNo_of_returningbooks.grid(row=5, column=0, sticky=W)
        txtNo_of_returningbooks = Entry(frame, font=("times new roman", 15, "bold"), width=29)
        txtNo_of_returningbooks.grid(row=5, column=1)

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1543, height=70)

        btnAddData = Button(Framebutton , text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1543, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        self.library_table = ttk.Treeview(Table_frame, column=("BookType", "BooksRecord", "BooksIssue", "NumberOfbooks", "NumberOfAvailableBooks", "NumberOfReturningBooks"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("BookType", text="Book Type")
        self.library_table.heading("BooksRecord", text="Books record")
        self.library_table.heading("BooksIssue", text="Books Issue")
        self.library_table.heading("NumberOfbooks", text="Number of books")
        self.library_table.heading("NumberOfAvailableBooks", text="Number of available books")
        self.library_table.heading("NumberOfReturningBooks", text="Number of returning books")


        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Book Type", width=100)
        self.library_table.column("Books record", width=100)
        self.library_table.column("Books Issue", width=100)
        self.library_table.column("Number of books", width=100)
        self.library_table.column("Number of available books", width=100)
        self.library_table.column("Number of returning books", width=100)


if __name__== "__main__":
    root=Tk()
    obj=Librarian(root)
    root.mainloop()
