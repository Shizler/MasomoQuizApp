from cmd import Cmd

from docopt import docopt, DocoptExit



#docopt(doc, argv=None, help=True, version=None, options_first=False)

class MyPrompt(Cmd):
	def do_hello(self,args):

		if len(args) == 0:
			name='stranger'
		else:
			name=args
		print ("Hello, %s" %name)


	
	def do_Quiz_List(self,arg):

		print ("Lists all available quizzes")

	def do_Quiz_Import(self,args):
		print ("Success")
	def do_quiz_take (self,args):
		print ("success")



	def do_quit(self,args):
		print ("Quitting")
		raise SystemExit


if __name__== '__main__':
	prompt =MyPrompt()
	prompt.prompt = 'masomoApp>'
	prompt.cmdloop('Starting prompt...')