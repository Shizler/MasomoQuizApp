import os
class ListQuiz():
    def find(self):
        path='C:/Users/andela/Documents/venv/MasomoQuizApp/quizzes/'
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".json"):
                   path_file = os.path.join(root,file)
                   files_got = file[:-5]
                   print (files_got)





