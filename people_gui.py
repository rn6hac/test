"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this script runs on, as 1 or more local files;
"""

import shelve
import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror

from const import SHELVE_NAME

DB = None
ENTRIES = {}

SEARCH_FIELD = 'SEARCH PERSON'
FIELD_NAMES = ('name', 'age', 'job', 'pay')


def make_widgets() -> tkinter.Tk:
    window = tkinter.Tk()
    window.title('People Shelve')
    window.geometry('300x300+600+400')
    form = tkinter.Frame(window)
    form.pack()

    lab = tkinter.Label(form, text=SEARCH_FIELD)
    values = tuple(DB.keys())
    combobox = ttk.Combobox(form, values=values)
    combobox.set('Select Person')
    ent = tkinter.Entry(form)
    lab.grid(row=0, column=0)
    ent.grid(row=0, column=1)
    ENTRIES[SEARCH_FIELD] = tkinter.Entry(form)

    for (ix, label) in enumerate(FIELD_NAMES):
        ent = tkinter.Entry(form)
        lab.grid(row=ix + 1, column=0)
        ent.grid(row=ix + 1, column=1)
        ENTRIES[label] = ent

    tkinter.Button(window, text="Fetch", command=fetch_record).pack(side=tkinter.LEFT)
    tkinter.Button(window, text="Update", command=update_record).pack(side=tkinter.LEFT)
    tkinter.Button(window, text="Quit", command=window.quit).pack(side=tkinter.RIGHT)

    return window


def fetch_record():
    full_name = ENTRIES[SEARCH_FIELD_NAME].get()
    if full_name is None:
        showerror(title='Error', message='No such key!')

    for field in FIELD_NAMES:
        ENTRIES[field].delete(0, tkinter.END)
        ENTRIES[field].insert(0, repr(getattr(DB[full_name], field)))


def update_record() -> None:
    full_name = ENTRIES[SEARCH_FIELD_NAME].get()
    if full_name is None:
        showerror(title='Error', message='No such key!')

    for field in FIELD_NAMES:
        setattr(DB[full_name], field, ENTRIES[field])


if __name__ == '__main__':
    try:
        DB = shelve.open(SHELVE_NAME)
        window = make_widgets()
        window.mainloop()
    finally:
        if DB:
            DB.close()
