import os
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format



def title():
    clear = lambda:os.system('cls')
    clear()
    init(strip = not sys.stdout.isatty())  # strip colors if stdout is redirected
    cprint(figlet_format('MASOMO', font = 'poison'),'yellow', attrs = ['bold'])



