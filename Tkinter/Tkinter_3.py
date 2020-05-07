"""
    Earlier we created a button and in the window and now, we cove the event hadling for it. We are going to add
    a quit event to our quit button, which currently does nothing when clicked on. In basically every circumstance,
    we're going to want to have our buttons actually do something or perform a action rather than just appear there.

    In Tkinter, event handling is as simple as adding a command, which we'll make into a function. Even though this
    function we create is a basic 1-line function that simply calls another function, we can see how we can later
    create more complex functions for our events.

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
        quitButton = Button(self, text="Quit", command= self.client_exit) # adding function to be called when event occurs

        # Placing the button on my window
        quitButton.place(x= 0, y= 0)

    # defining function to handle the event.
    def client_exit(self):
        exit()

root = Tk()

#Size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()
