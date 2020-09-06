from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


root = Tk()
root.title("To Do List")


def window(main):
    main.title('Checklist')
    main.update_idletasks()
    width=main.winfo_width()
    height=main.winfo_height()
    x=(main.winfo_screenwidth() // 2) - (width//2)
    y=(main.winfo_screenheight() // 2)-(height//2)
    main.geometry('{}x{}+{}+{}'.format(width,height,x,y))

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("/Users/yasminmodarai/Downloads/todolist.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

e=Example(root)
e.pack(fill=BOTH,expand=YES)

def insertitem():
    listbox.insert(tk.END,content.get())

def deletelist():
    listbox.delete(0,tk.END)

def deleteitemselected():
    listbox.delete(ANCHOR)

label1=Label(root,text="Enter a task:", bg="LightBlue2",fg="pink2",font="Saab 25")
label1.place(x=300,y=350)

content=tk.StringVar()
entry1=Entry(root, width=20,bg="LightBlue2",font="Saab 20",textvariable=content)
entry1.place(x=450,y=350)

button1=Button(root, text="Enter", bg="LightBlue2",fg="pink2",font="Saab 25",command=insertitem)
button1.place(x=450,y=400)
button2=Button(root,text="Delete list",bg="LightBlue2",fg="pink2",font="Saab 25",command=deletelist)
button2.place(x=450,y=430)
button3=Button(root,text="Delete selected item",bg="LightBlue2",fg="pink2",font="Saab 25",command=deleteitemselected)
button3.place(x=450,y=460)

listbox=tk.Listbox(root)
listbox.place(x=450,y=490)


root.mainloop()



