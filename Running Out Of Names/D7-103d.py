from tkinter import*
from PIL import ImageTk,Image
root = Tk()
root.geometry("600x600")
root.title("TitleUsed412thtime")
imagey = ImageTk.PhotoImage(Image.open("india.png"))

dic = {"India" : imagey}
inputy = Entry(root)



def function():
    
    try:
        inputget = inputy.get()
        button1['image'] = dic[inputget]
            
        
    except:
        print("Error day has come back")
        messagebox.showinfo("Error","Error day has come back")
        

button =Button(root,text="Text234timesused",command = function)
button1 =Button(root)
button.pack()
inputy.pack()
button1.pack()

root.mainloop()