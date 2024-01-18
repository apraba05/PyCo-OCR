import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = tk.Tk()
app.geometry("1500x1500")
app.title("PyCo")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=40, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome to PyCo")
label.pack(pady=20, padx=10)

my_label = customtkinter.CTkLabel(master=frame)
my_label.pack()

image_label = tk.Label(app)
image_label.pack()

def openFileExplorer():
    global my_image, image_label
    app.filename = filedialog.askopenfilename(
        initialdir="/Users/ashan",
        title="Select A File",
        filetypes=(("png files", "*.png"), ("all files", "*.*"), ("jpeg files", "*.jpeg"), ("jpg files", "*.jpg"))
    )
    my_label.config(text=app.filename)

    if app.filename:  # Check if a file was selected
        my_image = Image.open(app.filename)
        display_image = ImageTk.PhotoImage(my_image)
        
        # Update the existing image label to display the selected image
        image_label.config(image=display_image)
        image_label.image = display_image
        image_label.pack()  # Ensure the label is displayed
    else:
        my_label.config(text="No file selected")

button = customtkinter.CTkButton(master=frame, text="Start", command=openFileExplorer)
button.pack(pady=20, padx=15)

newLabel = tk.Label(master=frame, text="Upload a JPG or PNG")
newLabel.pack()

app.mainloop()
