from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save as a new file 
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        # save the file 
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("About Notepad", "Notepad by Jeetu")

if __name__=='__main__':
    # basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("1.ico")
    root.geometry("683x384")

    # text area 
    textArea = Text(root)
    file = None
    textArea.pack(fill=BOTH, expand=True)

    # menubar 
    menuBar = Menu(root)

    # file menu 
    fileMenu = Menu(menuBar, tearoff=0)

    # open new file 
    fileMenu.add_command(label="New", command=newFile)

    # open already existing file 
    fileMenu.add_command(label="Open", command=openFile)

    # save current file 
    fileMenu.add_command(label="Save", command=saveFile)

    fileMenu.add_separator()

    fileMenu.add_command(label="Exit", command=quitApp)

    menuBar.add_cascade(label="File", menu=fileMenu)

    # edit menu 
    editMenu = Menu(menuBar, tearoff=0)

    # cut, copy, paste
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    menuBar.add_cascade(label="Edit", menu=editMenu)

    # help menu 
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)

    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

    # scrollbar 
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)

    root.mainloop()