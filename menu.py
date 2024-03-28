from tkinter import *
from tkinter import ttk
from os import path
from tkinter.ttk import Combobox
from time import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import subprocess
import webbrowser
from vault import *

class Menu_cl():
    """
    main menu settings

    game_path: string
    current_os: string
    path_changed: bool
    _new_path: string

    default values:
        game_path: os.getcwd()
        current_os: "Windows x64"
        path_changed: False
        _new_path: ""
    """

    def __init__(self, game_path, current_os, path_changed, _new_path):
        """initializing settings"""
        
        Menu_cl.game_path = game_path
        Menu_cl.current_os = current_os
        Menu_cl.path_changed = path_changed
        Menu_cl._new_path = _new_path

    def support():
        """support me"""
        webbrowser.open("https://www.donationalerts.com/r/speedee6330")

    def apply():
        """applying all settings"""
        apply_ = messagebox.askyesno('Warning', 'Warning! Changing settings may cause unforeseen consequences (game crash). Continue?')
        if apply_:
            if combo_settings_os.get() != "GNU/Linux support soon":
                Menu_cl.current_os = combo_settings_os.get()
                set_ch(int(spin_challenge.get()))
                set_vol(int(spin_vol.get()) / 10)
                if Menu_cl.path_changed == False:
                    Menu_cl.game_path = combo_settings_game_folder.get()
                elif Menu_cl.path_changed == True:
                    Menu_cl.game_path = Menu_cl._new_path
                Menu_cl.path_changed = False
            else:
                messagebox.showerror("Critical error", "Variables 'current_os' can't be setted to this")
        else:
            None

    def change_game_path():
        """changing game path using interactive window"""
        
        global _new_path, path_changed
        _new_path = filedialog.askdirectory()
        path_changed = True

    def main_developer_matvei():
        """contact main developer"""
        webbrowser.open("https://t.me/MatMal29")
    
    def update_record():
        lbl_menu_text4.configure(text=read_r())

    def main(self):
        """running main menu window"""
        global menu_window, tab_control_menu, tab_help_menu, tab_main_menu, tab_settings_menu
        global lbl_menu_text1, lbl_menu_text2, lbl_menu_text3, lbl_menu_text4, btn_menu_play, btn_menu_quit, btn_menu_support
        
        global lbl_settings_folder, lbl_settings_os
        global btn_settings_apply, btn_settings_chnge_folder
        global combo_settings_game_folder, combo_settings_os, spin_challenge, spin_vol

        global lbl_help_contact, btn_help_contact2

        menu_window=Tk()
        menu_window.title("Menu")
        menu_window.geometry('400x250')
        tab_control_menu = ttk.Notebook(menu_window)

        tab_main_menu = ttk.Frame(tab_control_menu)
        tab_settings_menu = ttk.Frame(tab_control_menu)
        tab_help_menu = ttk.Frame(tab_control_menu)

        tab_control_menu.add(tab_main_menu, text='Main')
        tab_control_menu.add(tab_settings_menu, text='Settings')  
        tab_control_menu.add(tab_help_menu, text='Help')  

        #-------------------------------------tab_main_menu----------------------------------------------#
        lbl_menu_text1 = Label(tab_main_menu, text="Welcome to the game 'Asteroid shooter'", font=("Arial Bold", 16))
        lbl_menu_text2 = Label(tab_main_menu, text="You need to destroy asteroids", font=("Arial Bold", 13))
        lbl_menu_text3 = Label(tab_main_menu, text="Your record: ", font=("Arial Bold", 13))
        lbl_menu_text4 = Label(tab_main_menu, text="", font=("Arial Bold", 13))

        lbl_menu_text1.place(x=12, y=40)
        lbl_menu_text2.place(x=90, y=70)
        lbl_menu_text3.place(x=140, y=100)
        lbl_menu_text4.place(x=235, y=100)


        btn_menu_update = Button(tab_main_menu, text="Update record", command=Menu_cl.update_record)
        btn_menu_play = Button(tab_main_menu, text="PLAY", command=game)
        btn_menu_support = Button(tab_main_menu, text="SUPPORT", command=Menu_cl.support)
        btn_menu_quit = Button(tab_main_menu, text="QUIT", command=exit)

        btn_menu_update.place(x=157, y=135)
        btn_menu_play.place(x=20, y=180)
        btn_menu_support.place(x=170, y=180)
        btn_menu_quit.place(x=340, y=180)
        #-------------------------------------tab_main_menu----------------------------------------------#


        #-------------------------------------tab_settings_menu----------------------------------------------#
        lbl_settings_os = Label(tab_settings_menu, text="Current OS:")
        lbl_settings_folder = Label(tab_settings_menu, text="Game folder: ")
        lbl_settings_controls = Label(tab_settings_menu, text="Controls: " + "\n" + "WASD - movement" + "\n" + "SPACE - shoot", font=("Arial bold", 15))
        lbl_settings_challenge = Label(tab_settings_menu, text="Set challenge (sec):")
        lbl_settings_vol = Label(tab_settings_menu, text="Set volume:")

        lbl_settings_os.place(x=10, y=10)
        lbl_settings_folder.place(x=10, y=40)
        lbl_settings_controls.place(x=110, y=110)
        lbl_settings_challenge.place(x=10, y=70)
        lbl_settings_vol.place(x=180, y=70)

        combo_settings_os = Combobox(tab_settings_menu)
        combo_settings_os["values"] = ("Windows x64", "Windows x32", "GNU/Linux support soon")
        combo_settings_os.current(0)
        combo_settings_game_folder = Combobox(tab_settings_menu)
        combo_settings_game_folder["values"] = (Menu_cl.game_path, "You can change this value by typing here or use a button")
        combo_settings_game_folder.current(0)

        combo_settings_os.place(x=85, y=10)
        combo_settings_game_folder.place(x=85, y=40)


        btn_settings_chnge_folder = Button(tab_settings_menu, text="Change game folder...", command=Menu_cl.change_game_path)
        btn_settings_apply = Button(tab_settings_menu, text="Apply", command=Menu_cl.apply)
        btn_settings_reset = Button(tab_settings_menu, text="Reset all (current record and etc...)", command=default_s)
        btn_settings_vault = Button(tab_settings_menu, text="Vault", command=vault_gtk)
        btn_settings_console = Button(tab_settings_menu, text="Console", command=console)

        btn_settings_chnge_folder.place(x=230, y=38)
        btn_settings_apply.place(x=350, y=194)
        btn_settings_reset.place(x=7, y=194)
        btn_settings_vault.place(x=207, y=194)
        btn_settings_console.place(x=249, y=194)


        spin_challenge = Spinbox(tab_settings_menu, from_=0, to=600, width=5, textvariable=read_ch())
        spin_challenge.place(x=120, y=72)

        spin_vol = Spinbox(tab_settings_menu, from_=0, to=20, width=5, textvariable=read_vol() * 10)
        spin_vol.place(x=250, y=72)
        #-------------------------------------tab_settings_menu----------------------------------------------#


        #-------------------------------------tab_help_menu----------------------------------------------#
        lbl_help_contact = Label(tab_help_menu, text="You can contact me in Telegramm", font=("Arial bold", 18))

        lbl_help_contact.place(x=10, y=10)


        btn_help_contact2 = Button(tab_help_menu, text="Contact me", command=Menu_cl.main_developer_matvei, font=("Arial bold", 18))

        btn_help_contact2.place(x=120, y=50)
        #-------------------------------------tab_help_menu----------------------------------------------#

        tab_control_menu.pack(expand=1, fill='both')
        menu_window.mainloop()

def game():
    """runnig a game"""
    fold = "python " + '"' + Menu_cl.game_path + "\game.py" + '"'
    subprocess.call(fold, shell=True)
    print(fold)

def vault_gtk():
    fold = "python " + '"' + Menu_cl.game_path + "\\vault-gtk.py" + '"'
    subprocess.call(fold, shell=True)

def console():
    fold = "python " + '"' + Menu_cl.game_path + "\console.py" + '"'
    subprocess.call(fold, shell=True)


default = Menu_cl(path.join(path.dirname(__file__)), "Windows x64", False, "")
default.main()    # use this if programm not running via "main.py"