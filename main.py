from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext 
import os
from tkinter.ttk import Combobox
from time import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
import subprocess
import webbrowser
from menu import Menu_cl, default

type_speed_def = 0.05
game_path_def = os.getcwd()
current_os_def = "Windows x64"
path_changed_def = False


def menu_run():
    default.main()

# default = Menu_cl(os.getcwd(), "Windows x64", False)