from tkinter import*
from PIL import ImageTk, Image
gui = Tk()
gui.geometry('1550x800')
gui.title("Menu")
gui.bg = ImageTk.PhotoImage(file='C:\\Users\\Dell\\PycharmProjects\\ICT Solo project\\1.png')
gui.bg_image = Label(gui , image=gui.bg).place(x=0, y=0, relwidth=1, relheight=1)


# Open the Image File
bg = ImageTk.PhotoImage(file="1.png")

# Create a Canvas
canvas = Canvas(gui, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("1.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# Bind the function to configure the parent window
gui.bind("<Configure>", resize_image)


librarian_but=Button(gui,cursor="hand2",text="Librarian",bg="#d77337",fg="white",font=("times new roman",20,'bold')).place(x=605,y=220,width=350,height=150)
student_but=Button(gui,cursor="hand2",text="Student",bg="#d77337",fg="white",font=("times new roman",20,'bold')).place(x=605,y=450,width=350,height=150)
gui.mainloop()
