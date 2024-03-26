import pickle
from tkinter import messagebox

record_d = 0
ch_d = 0

def default_call():
    with open('ch.sav', 'wb') as f:
        pickle.dump(ch_d, f)

    with open('rec.sav', 'wb') as f:
        pickle.dump(record_d, f)


def default_s():
    run = messagebox.askyesno("WARNING", "This will reset all your progress. Continue?")
    """use this only once to set values to default"""

    if run:
        with open('ch.sav', 'wb') as f:
            pickle.dump(ch_d, f)

        with open('rec.sav', 'wb') as f:
            pickle.dump(record_d, f)

def set_r(val):
    with open('rec.sav', 'wb') as f:
        pickle.dump(val, f)

def set_ch(val):
    with open("ch.sav", "wb") as f:
        pickle.dump(val, f)

def read_r():
    with open('rec.sav', 'rb') as f:
        rec = pickle.load(f)
    return rec

def read_ch():
    with open('ch.sav', 'rb') as f:
        ch = pickle.load(f)
    return ch

# default() # !!!WARNING!!! uncomment it only if you wanna reset your record and challenge!!!