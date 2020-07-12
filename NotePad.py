from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# File Functions...
def newFile():
    global file
    root.title("Untititled - NotePad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                              filetypes=[("All Files", "*.*"),
                                         ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", ".*.Txt")])
        if file == "":
            file=None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

# Edit functions...
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

# about fuctions...
def about():
    showinfo("Notepad", "NotePad by Prabir")


if __name__ == '__main__':
    # basic tkinter setup...
    root  = Tk()
    root.title("Untiteled - Notepad")
    root.wm_iconbitmap("Noteicon.ico")
    root.geometry("880x645")

    # add textArea
    TextArea = Text(root, font="calibri 20", bg="white", borderwidth=0, relief=RAISED)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

# create menubar
    main_menu = Menu(root)

    # FIle Menu
    m1 = Menu(main_menu, tearoff=0)
    m1.add_command(label="New                               Ctrl+N ", command=newFile)
    m1.add_command(label="New Window     Ctrl+Shift+N ")
    m1.add_command(label="Open...                           Ctrl+O ", command=openFile)
    m1.add_command(label="Save                                Ctrl+S ", command=saveFile)
    m1.add_command(label="Save as...              Ctrl+Shift+S ")
    m1.add_separator()
    m1.add_command(label="Page setup...")
    m1.add_command(label="Print...                             Ctrl+P ")
    m1.add_separator()
    m1.add_command(label="Exit", command=quitApp)
    root.config(menu=main_menu)
    main_menu.add_cascade(label="File", menu=m1)

    # Edit Menu
    m2 = Menu(main_menu, tearoff=0)
    m2.add_command(label="Undo                                 Ctrl+Z ")
    m2.add_separator()
    m2.add_command(label="Cut                                     Ctrl+X ", command=cut)
    m2.add_command(label="Copy                                  Ctrl+C ", command=copy)
    m2.add_command(label="paste                                  Ctrl+V ", command=paste)
    m2.add_command(label="Delete                                     Del ")
    m2.add_separator()
    m2.add_command(label="Find                                   Ctrl+F ")
    root.config(menu=main_menu)
    main_menu.add_cascade(label="Edit", menu=m2)

    # Format Menu
    m3 = Menu(main_menu, tearoff=0)

    root.config(menu=main_menu)
    main_menu.add_cascade(label="Format", menu=m3)

    # Format Menu
    m4 = Menu(main_menu, tearoff=0)

    root.config(menu=main_menu)
    main_menu.add_cascade(label="View", menu=m4)

    # Help Menu
    m5 = Menu(main_menu, tearoff=0)
    m5.add_command(label="About", command=about)
    m5.add_command(label="Rate Us")
    main_menu.add_cascade(label="Help", menu=m5)

# Create Scrollbar
    # YscrollBar
    scroll = Scrollbar(TextArea)
    scroll.pack(fill=Y, side=RIGHT)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    # XscrollBar
    scroll = Scrollbar(TextArea, orient="horizontal")
    scroll.pack(fill=X, side=BOTTOM)
    scroll.config(command=TextArea.xview)
    TextArea.config(xscrollcommand=scroll.set)


# Create StatusBar
    var = StringVar()
    var.set("UTF - 8             ")
    statusbar = Label(root, textvar=var, relief=RAISED, anchor=E, borderwidth=0)
    statusbar.pack(side=BOTTOM, fill=X)

    root.mainloop()
