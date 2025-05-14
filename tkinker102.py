from tkinter import *
from tkinter.messagebox import showinfo


class my_gui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button prese!')

if __name__ == '__main__':
    window = my_gui()
    window.pack()
    window.mainloop()


