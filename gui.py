import customtkinter
from tkinter import Image
from customtkinter import *
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

fileExact = "/Users/ashan"
result = True
info = ""
app = CTk()
app.geometry("500x400+600+300")
app.title("PyCo")

ico = Image.open("/Users/ashan/Documents/PyCo.icns")
photo = ImageTk.PhotoImage(ico)
app.wm_iconphoto(False,photo)

customtkinter.set_appearance_mode("System")

label = CTkLabel(master=app, text="Welcome to PyCo",font = ("San Francisco",30))
label.pack(pady=20, padx=10)

button = CTkButton(master = app, text = "Start",font = ("Sultan",20), command = openFileExplorer, corner_radius=32, fg_color= "transparent",hover_color="#4158D0",border_color="#FFCC70",border_width=2)
button.place (relx = 0.5,rely = 0.5, anchor = "center")
button.pack()

combobox = CTkComboBox(master = app, values=["Python"],fg_color="#0093E9",border_color="#FBAB7E",dropdown_fg_color="#0093E9")
combobox.place (relx = 0.5,rely = 0.7,anchor = "center")

label = CTkLabel(master=app, text="\nPyCo is a revolutionary application designed to simplify\n the process of executing handwritten code! Using image\n recognition, you will be able to effortlessly translate code\n on paper into executable output.",font = ("GT America",18))
label.place(relx = 0.5,rely = 0.6, anchor = "s")
