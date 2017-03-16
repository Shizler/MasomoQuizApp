"""
Usage:
    masomo quiz_list
    masomo quiz_import <path_to_quiz_JSON>
    masomo quiz_take <quiz_name>
    masomo (-i | --interactive)
    masomo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    
"""

import sys
import os
import cmd
# from app.amity import Amity
from docopt import docopt, DocoptExit
from listsquiz import ListQuiz


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

q=ListQuiz()

class MasomoSystem(cmd.Cmd):
    intro = 'Welcome to Masomo' \
        + ' (type help for a list of commands.)'
    prompt = '(Masomo) '
    file = None

    @docopt_cmd
    def do_quiz_list(self,args):
        """Usage: quiz_list..."""
        q.find()
        

    @docopt_cmd
    def do_quiz_import(self, args):
        """Usage: quiz_import <path_to_quiz_JSON>..."""
        print ("success")
    @docopt_cmd
    def do_quiz_take(self, args):
        """Usage: quiz_take<quiz_name>..."""
        result
        print ("success")


    def do_clear(self, arg):
        """Clears screen>"""

        os.system('clear')

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
   MasomoSystem().cmdloop()

print(opt)