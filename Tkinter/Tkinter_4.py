"""
    Now that we've go the basic window, buttons, and event handling down, we're ready to tackle the idea of a menu
    bar. The way tkinter works, along with quite a few graphics/windows operations work, is with a main window,
    then you sort of build things on top of it, then display everything all at once, which gives the appearance of
    a singular package.
"""

from tkinter import *

class Window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill= BOTH, expand= 1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu= menu)

        #Create the file object
        file = Menu(menu)
        # add a command to the menu option, calling it exit, and the command it runs on event is client_exit
        file.add_command(label= "Exit", command = self.client_exit)

        # add "file" to our menu
        menu.add_cascade(label= "File", menu= file)

        # create edit object
        edit = Menu(menu)

        edit.add_command(label= "Undo")
        menu.add_cascade(label= "Edit", menu= edit)

    def client_exit(self):
        exit()


root = Tk()

#Size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()
