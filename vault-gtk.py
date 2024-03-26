from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

def clear_():
    console.delete(1.0, END)

def cmd_(out: str, bash = False):
    if bash:
        console.insert(END, ">>> " + out + "\n")
    else:
        console.insert(END, out + "\n")

def new_ch():
    cmd_("ch=" + in_ch.get(), True)
    cmd_("trying to set challenge to " + in_ch.get() + "...")
    try:
        set_ch(int(in_ch.get()))
        cmd_("challenge succesfuly setted to " + in_ch.get())
    except:
        cmd_("unexpected error!")


def new_rec():
    cmd_("rec=" + in_rec.get(), True)
    cmd_("trying to set record to " + in_rec.get() + "...")
    try:
        set_r(int(in_rec.get()))
        cmd_("record succesfuly setted to " + in_rec.get())
    except:
        cmd_("unexpected error!")

def r_rec():
    cmd_("rec", True)
    cmd_("record:" + str(read_r()))

def r_ch():
    cmd_("ch", True)
    cmd_("challenge:" + str(read_ch()))

def default_s_check():
    cmd_("reset_()", True)
    cmd_("Reset?")
    cmd_("This will set this settings: \n   record:0\n   challenge:0")
    cmd_("y / n:")
    do = messagebox.askokcancel("Reset?", "This will set this settings: \nrecord: 0\nchallenge: 0")
    if do:
        cmd_("$ y")
        cmd_("reseting all...")
        default_call()
        cmd_("all settings reset")
    else:
        cmd_("$ n")
        cmd_("operation canceled")

window = Tk()
window.geometry("400x216")
window.title("Vault control")

btn_ch = Button(window, text="Set new value", command=new_ch)
btn_rec = Button(window, text="Set new value", command=new_rec)

btn_ch_r = Button(window, text="Read value", command=r_ch)
btn_rec_r = Button(window, text="Read value", command=r_rec)

btn_res = Button(window, text="RESET", command=default_s_check, width=10)
btn_clr = Button(window, text="CLEAR", command=clear_, width=10)

btn_ch_r.place(x=230, y=-4)
btn_rec_r.place(x=230, y=21)

btn_ch.place(x=140, y=-4)
btn_rec.place(x=140, y=21)

btn_res.place(x=300, y=-4)
btn_clr.place(x=300, y=21)


lbl_ch = Label(window, text="Challenge:")
lbl_rec = Label(window, text="Record:")

lbl_ch.place(x=0, y=0)
lbl_rec.place(x=0, y=25)


in_ch = Entry(window, width=10)
in_rec = Entry(window, width=10)

in_ch.place(x=70, y=0)
in_rec.place(x=70, y=25)


console = scrolledtext.ScrolledText(window, height=10, width=47)
console.place(x=0, y=50)

cmd_("vault", True)
try:
    global read_ch, read_r, set_ch, set_r, default_call
    from vault import read_ch, read_r, set_ch, set_r, default_call
    cmd_("vault succesfully imported")
    cmd_("to use graphics use 'vault-gtk'")
except:
    cmd_("cannot get access to vault.py")

window.mainloop()