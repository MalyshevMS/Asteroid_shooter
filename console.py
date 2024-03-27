from tkinter import *
from tkinter import scrolledtext
from os import path
import subprocess
import keyboard

folder = path.join(path.dirname(__file__))
bash = ">>> "
shell = False
vault = False
do = False
ask = False

def s_return(a):
    send_()

def send_():
    echo(in_.get(), True)
    exe(in_.get())

def echo(txt, bash_ = False):
    if bash_:
        out.insert(END, bash + txt + "\n")
    else:
        out.insert(END, txt + "\n")

def exe(com: str):
    """executing command (com) in console window"""
    global bash, shell
    if not shell:
        if com[:4] == "echo":
            echo(com[5:])
    
        elif com == "quit" or com == "exit":
            try: exit()
            except: quit()
    
        elif com[:4] == "bash":
            bash = com[5:]
            echo("new bash:" + bash)
    
        elif com == "vault" or com == "vault()":
            echo("trying to import vault...")
            try:
                global read_ch, read_r, set_ch, set_r, default_call, read_deaths, read_kill, set_deaths, set_kill
                from vault import read_ch, read_r, read_deaths, read_kill, set_ch, set_r, set_deaths, set_kill, default_call
                echo("vault succesfully imported")
                echo("to use graphics use 'vault-gtk'")
            except:
                echo("cannot get access to vault.py")

        elif com[:3] == "ch=":
            echo("trying to set challenge to " + com[3:] + "...")
            try:
                set_ch(int(com[3:]))
                echo("challenge succesfuly setted to " + com[3:])
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")

        elif com[:4] == "rec=":
            echo("trying to set record to " + com[4:] + "...")
            try:
                set_r(int(com[4:]))
                echo("record succesfuly setted to " + com[4:])
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")

        elif com[:5] == "kill=":
            echo("trying to set kill to " + com[5:] + "...")
            try:
                set_kill(int(com[5:]))
                echo("kill succesfuly setted to " + com[5:])
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")

        elif com[:7] == "deaths=":
            echo("trying to set deaths to " + com[7:] + "...")
            try:
                set_deaths(int(com[7:]))
                echo("deaths succesfuly setted to " + com[7:])
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")
        
        elif com == "rec()" or com == "rec":
            try: echo("record:" + str(read_r()))
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")
        
        elif com == "ch()" or com == "ch":
            try: echo("challenge:" + str(read_ch()))
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")
            

        elif com == "kill" or com == "kill()":
            try: echo("kills:" + str(read_kill()))
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")

        elif com == "deaths" or com == "deaths()":
            try: echo("deaths:" + str(read_deaths()))
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import valut")
        
        elif com == "game":
            echo("starting game...")
            echo("to use console close game window")
            subprocess.call("python " + '"' +folder + "\game.py" + '"', shell=True)
        
        elif com == "menu":
            echo("starting menu...")
            echo("to use console close menu window")
            subprocess.call("python " + '"' + folder + "\menu.py" + '"', shell=True)

        elif com == "vault-gtk":
            echo("starting vault-gtk...")
            echo("to use console close vault-gtk window")
            subprocess.call("python " + '"' + folder + "\\vault-gtk.py" + '"', shell=True)

        elif com == "shell" or com == "cmd":
            bash = "cmd: "
            echo("now commands will be redirected to cmd.exe with bash:\n" + '\t"' + bash + '"')
            echo("to escape use 'exit'")
            shell = True

        elif com[:4] == "help":
            if com == "help":
                show_coms()
            else:
                get_help(com[5:])

        elif com == "clear":
            clear_()

        elif com == "default_" or com == "default_()":
            try:
                echo("reseting all...")
                default_call()
                echo("all settings reset")
            except:
                echo("unexpected error!")
                echo("maybe you forgot to import vault")

        else:
            echo("ERROR: command " + com + " are not existing or can not be used")

    elif shell:
        if com == "exit":
            echo("exiting cmd...")
            bash = ">>> "
            shell = False
        else:
            echo(subprocess.getoutput(com))
            # except: echo("ERROR: command are not existing or can not be used")


def clear_():
    out.delete(1.0, END)

def show_coms():
    echo("list of available commands:")
    echo("\techo")
    echo("\tquit")
    echo("\tbash")
    echo("\tch=")
    echo("\trec=")
    echo("\tkill=")
    echo("\tdeaths=")
    echo("\trec or rec()")
    echo("\tch or ch()")
    echo("\tkill or kill()")
    echo("\tdeaths or deaths()")
    echo("\tmenu")
    echo("\tgame")
    echo("\tvault")
    echo("\tvault-gtk")
    echo("\tshell or pwsh")
    echo("\tclear")
    echo("\tdefault_ or default_()")
    echo("\ncommands rec, rec(), ch, ch(), deaths, deaths(), kill, \nkill(), ch=, rec=, kill=, deaths=, default_, default_() \nruns only after 'vault' command")

def get_help(com):
    if com == "echo":
        echo("prints value after 'echo' in console")
    
    elif com == "quit":
        echo("exit console")
    
    elif com == "bash":
        echo("changing default bash '>>> ' to bash, typed after 'bash'")
    
    elif com == "vault" or com == "vault()":
        echo("import vault, to use vault operators")

    elif com == "ch=":
        echo("needs to import vault\nset variable challenge to value after '='")

    elif com == "rec=":
         echo("needs to import vault\nset variable record to value after '='")

    elif com == "kill=":
         echo("needs to import vault\nset variable kill to value after '='")

    elif com == "deaths=":
         echo("needs to import vault\nset deaths record to value after '='")

    elif com == "rec()" or com == "rec":
        echo("needs to import vault\nreads record value")

    elif com == "ch()" or com == "ch":
        echo("needs to import vault\nreads record value")

    elif com == "kill()" or com == "kill":
        echo("needs to import vault\nreads kill value")

    elif com == "deaths()" or com == "deaths":
        echo("needs to import vault\nreads deaths value")

    elif com == "game":
        echo("starts game (to use console close game window)")

    elif com == "menu":
        echo("starts menu (to use console close menu window)")

    elif com == "vault-gtk":
        echo("starts graphic version of vault (to use console close vault-gtk window)")

    elif com == "shell" or com == "pwsh":
        echo("redirect commands to cmd.exe with bash 'PS: '")
        echo("to stop use Pstop command")

    elif com == "clear":
        echo("clearing console")
    
    elif com == "default_" or "default_()":
        echo("needs to import vault\nreset challenge and record to default:\n\trecord:0\n\tchallnge:0")

    else:
        echo("unknown command")

cmd = Tk()
cmd.geometry("500x354")
cmd.title("Console")

out = scrolledtext.ScrolledText(cmd, width=59, height=20)
out.place(x=0, y=0)

in_ = Entry(cmd, width=59)
in_.place(x=0, y=330)
in_.focus()

send = Button(cmd, text="Send" , command=send_)
send.place(x=360, y=328)

clear = Button(cmd, text="Clear all", command=clear_)
clear.place(x=402, y=328)

ext = Button(cmd, text="QUIT", command=quit)
ext.place(x=460, y=328)

cmd.bind("<Return>", s_return)

cmd.mainloop()