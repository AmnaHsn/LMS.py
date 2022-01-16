from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",port=3306,password="",database="library management system")
cursor= conn.cursor()
selectquery="select * from librarian"
cursor.execute(selectquery)
records=cursor.fetchall()
print("librarian", cursor.rowcount)

for row in records:
  print("Librarian_name",row[0])
  print("Librarian_ID",row[1])
  print()

cursor.close()
conn.close()

class Login:
   def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1199x1498+100+50")
        self.root.resizable(False,False)
        self.bg =ImageTk.PhotoImage(file='C:\Library Management System\\library.png')
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
       
        # Create a Canvas
        canvas = Canvas(self.root, width=700, height=3500)
        canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
        canvas.create_image(0, 0, image=self.bg, anchor='nw')

# Function to resize the window
        def resize_image(e):
             global image, resized, image2
   # open image to resize it
             image = Image.open(".png")
   # resize the image with width and height of root
             resized = image.resize((e.width, e.height), Image.ANTIALIAS)

             image2 = ImageTk.PhotoImage(resized)
             canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
             self.root.bind("<Configure>", resize_image)


#login frame
        frame_login=Frame(self.root,bg="white")
        frame_login.place(x=360,y=350,height=340,width=400)

        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(frame_login,text="Enter your login details Here",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=80,y=100)
        lbl_user=Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=80,y=140)
        self.txt_user=Entry(frame_login ,font=("times new roman",15),bg="lightgrey")
        self.txt_user.place(x=80,y=170,width=300,height=35)

        lbl_pass=Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=80,y=210)
        self.txt_pass=Entry(frame_login ,font=("times new roman",15),bg="lightgrey",show="*")
        self.txt_pass.place(x=80,y=240,width=300,height=35)

    
        forget=Button(frame_login,text="Forget Passward?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=80,y=280)
        login_but=Button(self.root,cursor="hand2",text="login",bg="#d77337",fg="white",font=("times new roman",20)).place(x=470,y=660,width=180,height=40)
#working    

root=Tk()
obj=Login(root)
root.mainloop()
