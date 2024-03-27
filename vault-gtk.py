from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

def clear_():
    console.delete(1.0, END)

def echo(out: str, bash = False):
    if bash:
        console.insert(END, ">>> " + out + "\n")
    else:
        console.insert(END, out + "\n")

def new_ch():
    echo("ch=" + in_ch.get(), True)
    echo("trying to set challenge to " + in_ch.get() + "...")
    try:
        set_ch(int(in_ch.get()))
        echo("challenge succesfuly setted to " + in_ch.get())
    except:
        echo("unexpected error!")

def new_rec():
    echo("rec=" + in_rec.get(), True)
    echo("trying to set record to " + in_rec.get() + "...")
    try:
        set_r(int(in_rec.get()))
        echo("record succesfuly setted to " + in_rec.get())
    except:
        echo("unexpected error!")

def new_kill():
    echo("kill=" + in_kill.get(), True)
    echo("trying to set kill to " + in_kill.get() + "...")
    try:
        set_ch(int(in_kill.get()))
        echo("kill succesfuly setted to " + in_kill.get())
    except:
        echo("unexpected error!")

def new_deaths():
    echo("deaths=" + in_deaths.get(), True)
    echo("trying to set deaths to " + in_deaths.get() + "...")
    try:
        set_ch(int(in_kill.get()))
        echo("deaths succesfuly setted to " + in_deaths.get())
    except:
        echo("unexpected error!")

def r_rec():
    echo("rec", True)
    echo("record:" + str(read_r()))

def r_ch():
    echo("ch", True)
    echo("challenge:" + str(read_ch()))

def r_kill():
    echo("kill", True)
    echo("kill:" + str(read_kill()))

def r_deaths():
    echo("deaths", True)
    echo("deaths:" + str(read_deaths()))

def default_s_check():
    echo("reset_()", True)
    echo("Reset?")
    echo("This will set this settings: \n   record:0\n   challenge:0")
    echo("y / n:")
    do = messagebox.askokcancel("Reset?", "This will set this settings: \nrecord: 0\nchallenge: 0\nkill: 0\ndeaths: 0")
    if do:
        echo("$ y")
        echo("reseting all...")
        default_call()
        echo("all settings reset")
    else:
        echo("$ n")
        echo("operation canceled")

window = Tk()
window.geometry("357x270")
window.title("Vault control")

btn_ch = Button(window, text="Set new value", command=new_ch)
btn_rec = Button(window, text="Set new value", command=new_rec)
btn_kill = Button(window, text="Set new value", command=new_kill)
btn_deaths = Button(window, text="Set new value", command=new_deaths)

btn_ch.grid(column=2, row=0)
btn_rec.grid(column=2, row=1)
btn_kill.grid(column=2, row=2)
btn_deaths.grid(column=2, row=3)


btn_ch_r = Button(window, text="Read value", command=r_ch)
btn_rec_r = Button(window, text="Read value", command=r_rec)
btn_kill_r = Button(window, text="Read value", command=r_kill)
btn_deaths_r = Button(window, text="Read value", command=r_deaths)

btn_ch_r.grid(column=3, row=0)
btn_rec_r.grid(column=3, row=1)
btn_kill_r.grid(column=3, row=2)
btn_deaths_r.grid(column=3, row=3)


btn_res = Button(window, text="RESET", command=default_s_check, width=10)
btn_clr = Button(window, text="CLEAR", command=clear_, width=10)

btn_res.grid(column=4, row=1)
btn_clr.grid(column=4, row=2)


lbl_ch = Label(window, text="Challenge:")
lbl_rec = Label(window, text="Record:")
lbl_kill = Label(window, text="Kill:")
lbl_deaths = Label(window, text="Deaths:")

lbl_ch.grid(column=0, row=0)
lbl_rec.grid(column=0, row=1)
lbl_kill.grid(column=0, row=2)
lbl_deaths.grid(column=0, row=3)


in_ch = Entry(window, width=10)
in_rec = Entry(window, width=10)
in_kill = Entry(window, width=10)
in_deaths = Entry(window, width=10)

in_ch.grid(column=1, row=0)
in_rec.grid(column=1, row=1)
in_kill.grid(column=1, row=2)
in_deaths.grid(column=1, row=3)


console = scrolledtext.ScrolledText(window, height=10, width=42)
console.place(x=0, y=105)

echo("vault", True)
try:
    global read_ch, read_r, read_deaths, read_kill, set_ch, set_r, set_deaths, set_kill, default_call
    from vault import read_ch, read_r, read_deaths, read_kill, set_ch, set_r, set_deaths, set_kill, default_call
    echo("vault succesfully imported")
    echo("to use graphics use 'vault-gtk'")
except: echo("cannot get access to vault.py")

window.mainloop()