from PIL import ImageTk, Image
import os
import pytesseract
import PIL.Image

def openFileExplorer():
   global fileName,img,info,fileExact
   fileName = filedialog.askopenfilename(initialdir= "/Users/ashan",title = "Select A File",filetypes = (("png files","*.png"),("all files","*.*"),("jpeg files","*.jpeg"),("jpg files","*.jpg")))
   img = Image.open(fileName)
   fileExact = os.path.basename(fileName).split('/')[-1]
   result = messagebox.askyesno(
      title = 'Yes or No',
      message = "Please Confirm if this is the image you would like to upload.",
      detail = fileExact
   )
   if result:   
            try:
                info = pytesseract.image_to_string(PIL.Image.open(fileName),config=r"--psm 6 --oem 3")
                compiled_code = compile(info, '<string>', 'exec')
                exec(compiled_code)
            except Exception as e:
                newWindow = Toplevel()
                newWindow.geometry("500x400+600+300")
                errorLabel = CTkLabel(master= newWindow, text="Error Executing Python Code", font=("Arial", 20))
                errorLabel.pack(pady=20, padx=10)

app.mainloop()



