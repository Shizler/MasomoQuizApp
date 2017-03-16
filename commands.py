"""
Usage:
    masomo quiz_list
    masomo quiz_import <path_to_quiz_JSON>
    masomo take_quiz <quiz_name>
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from list_quiz import ListQuiz
from reading_json import QuizTake


def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
           
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
          
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

# creating an instance of class ListQuiz
q=ListQuiz()

# creating an instance of class QuizTake
r=QuizTake()
class MasomoSystem(cmd.Cmd):
    # welcomes the user
    intro = 'Welcome to Masomo' \
        + ' (type help for a list of commands.)'
    prompt = '(Masomo) '
    file = None

    # listing the commands

    @docopt_cmd
    def do_quiz_list(self,args):
        """Usage: quiz_list"""
        # calls the 'find' function in list_quiz file
        # returns the list of quizzes available in my library
        q.find()
    @docopt_cmd
    def do_quiz_import(self, args):
        """Usage: quiz_import <path_to_quiz_JSON>"""
        print ("success")

    @docopt_cmd
    def do_take_quiz(self, args):
        """Usage: take_quiz <quiz_name>"""
        '''make a var name_quiz that takes in the <quiz_name> input by the user.
        this var is passed to read_file function in reading_json file to retrieve 
        its url,then then display the quiz'''
        name_quiz = args["<quiz_name>"]
        r.read_file(name_quiz)


    def do_clear(self, arg):
        # Clears the screen

        os.system('clear')

    def do_quit(self, arg):
        # Quits out of the system

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
   MasomoSystem().cmdloop()

print(opt)