from tkinter import *
from tkinker102 import my_gui

# main app window
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
my_gui(popup).pack(side=RIGHT)                   # attach my frame
mainwin.mainloop()