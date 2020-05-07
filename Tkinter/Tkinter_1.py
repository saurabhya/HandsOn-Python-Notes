"""
    The Tkinter module is a wrapper around tk, which is a wrapper around tcl, which is used to create windows and
    graphical user interfaces Here, we see how simple it is to create a very basic window. we get a window that
    can resize, minimize, maximize and close! The tkinter module's purpose is to generate GUIs. Python is not very
    popularly used for this purpose, but it is more than capable of doing it.
"""
# Simple enough, just import everything from tkinter.

from tkinter import *

"""
    Here, we are creating our class, Window and inheriting from the Frame class. Frame is a class from the tkinter
    module.
    Then we define the settings upon initialization. This is the master widget.
"""

class window(Frame):
    def __init__(self, master= None):
        Frame.__init__(self, master)
        self.master = master

"""
    The above is all we need to do to get a window instance started.
    Root window created. Here, that would be the only window, but you can later have windows within windows.
"""
root = Tk()
# Then we actually create the instance
app = window(root)
# Finally show it and begin the main loop.
root.mainloop()