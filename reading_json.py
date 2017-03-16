from threading import Thread
import json
import time 
import os
from shutil import copyfile, move
import click
class QuizTake():
  # def timer():
  #   print ('time started...')
  #   for i in xrange(10,0,-1):
  #     time.sleep(1)
  #     time_remaining -= 1;
  #     print ('Time remaining: %d seconds\r '% i,)

  #     sys.stdout.flush()

  def read_file(self,name):
    # receives <quiz_name> as in argument name
    # arg is passed to retrieve the particular quiz
    file_path =''
    path='C:\\Users\\andela\\Documents\\venv\\MasomoQuizApp\\quizzes\\'
    for root, dirs, files in os.walk(path):
        for file in files:
           if file == name+'.json':
              file_path = os.path.join(root,file)

    if file_path =='':
      # checks if user has input a quiz not available
       print ("Quiz not found")
    else:
      # opens,reads and loads the json file
      json_data = open(file_path).read() 
      data = json.loads(json_data) 

      # initializes the var answerlist that stores the score
      answersList = 0
      # enumerate loops over something and has an automatic counter
      # prints the question and answer
      for index, question in enumerate(data): 
        click.secho('********************************************************************************',fg='cyan')
        print (index+1, question['question']) 
        print ("A:"+ question['A']) 
        print ("B:"+ question['B']) 
        print ("C:"+ question['C']) 
        print ("D:"+ question['D']) 

        

        answers=input('Enter your answer')
        if answers.isalpha():

          if question['answer'] == answers:
           answersList += 1
           print ("Correct Answer")
          else:
           print ("Incorrect answer.The correct answer is " + question['answer'])
           print ('\n') 
        else:
          print ("Invalid input.Please input A,B,C or D")



          print("You got {} answers right".format(answersList))
  def import_quiz(self,path):
      print (path)
      for root, dirs, files in os.walk(path):
        for file in files:
           if file.endswith('.json'):
              file_path = os.path.join(root,file)
              dest='C:/Users/andela/Documents/venv/MasomoQuizApp/quizzes'
              print(file_path)
              move(file_path,dest)
              print ("successfully")

  #             print(time_remaining)
  # timer()
  # t1=Thread(target=timer)
  # t2=Thread(target=read_file)
  # t1.start()
  # t2.start()
