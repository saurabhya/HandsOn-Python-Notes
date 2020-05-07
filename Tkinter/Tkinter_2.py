"""
    Buttons

    Once you've figured out the basics to a tkinter window, you might fancy the addition of some buttons.
    Buttons are used for all sorts of things, but generally are great to incite some interaction between
    the program and the user. Adding buttons is a two-fold thing in Python. The addition of the button
    and then its functionality. Let us first add the button and we will worry about its functionality later.
"""

from tkinter import *
class Window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # Changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill= BOTH, expand= 1)

        #creating a button instance
        quitButton = Button(self, text="Quit")

        # Placing the button on my window
        quitButton.place(x= 0, y= 0)

root = Tk()

#Size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()

"""
    Why self.init_window() - Genrally we refer a "window" as a frame. So that outer edge that people generally
    call a window is actually a frame.
    So, once you have created the frame, you need to specify some rules to the window within it. Here, we
    initialize the actual window, which we begin to modify. The next major thing we see is the init_window() function
    in our window class. Here, we give the window a title, which adds the title to the GUI. Then we pack, which
    allows our widget to take the full space of ou root window, or frame.
"""