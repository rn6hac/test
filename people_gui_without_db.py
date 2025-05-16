"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this script runs on, as 1 or more local files;
"""

import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

import const

DB = None

ENTRIES = {}

SEARCH_FIELD = 'SEARCH PERSON'
FIELD_NAMES = ('name', 'age', 'job', 'pay')


def get_selected_person_full_name() -> str:
    full_name = ENTRIES[SEARCH_FIELD].get()
    if full_name is None:
        showerror(title='Error', message='No such key!')
    return full_name


def make_widgets() -> tkinter.Tk:
    window = tkinter.Tk()
    window.title('People Shelve')
    window.geometry('300x300+600+400')
    form = tkinter.Frame(window)
    form.pack()

    values = tuple(DB.keys())
    combobox = ttk.Combobox(form, values=values)
    combobox.config(state='readonly')
    lab = tkinter.Label(form, text='SEARCH')
    lab.grid(row=0, column=0)
    combobox.set('Select Person')
    combobox.grid(row=0, column=1)
    combobox.bind('<<ComboboxSelected>>', fetch_record)
    ENTRIES[SEARCH_FIELD] = combobox

    for (ix, label) in enumerate(FIELD_NAMES):
        ent = tkinter.Entry(form)
        lab = tkinter.Label(form, text=label)
        lab.grid(row=ix + 1, column=0)
        ent.grid(row=ix + 1, column=1)
        ENTRIES[label] = ent

    tkinter.Button(window, text="Update", command=update_record).pack(side=tkinter.LEFT)
    tkinter.Button(window, text="Quit", command=window.quit).pack(side=tkinter.RIGHT)

    return window


def fetch_record(event: tkinter.Event):
    full_name = get_selected_person_full_name()

    for field in FIELD_NAMES:
        ENTRIES[field].delete(0, tkinter.END)
        ENTRIES[field].insert(0, repr(getattr(DB[full_name], field)))

    showinfo('Fetched', f'{full_name} person info fetched')


def update_record() -> None:
    full_name = get_selected_person_full_name()

    for field in FIELD_NAMES:
        record = DB[full_name]
        setattr(record, field, ENTRIES[field].get())

    showinfo('Updated', f'{full_name} person info updated')


if __name__ == '__main__':
    DB = {
        const.BOB.name: const.BOB,
        const.TOM.name: const.TOM,
        const.SUE.name: const.SUE,
    }
    window = make_widgets()
    window.mainloop()
