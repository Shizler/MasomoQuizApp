
import json
import time 

def read_file(): 

    # accesses the json file
    # start=time.time()
    path ='C:\\Users\\andela\\Documents\\MasomoProject\\quiz.json'
    # add var of quiz at the end of path
    json_data=open(path).read() 

 
    data=json.loads(json_data) 

    # initializes the var answerlist that stores the score

    answersList = 0
 
    for index, question in enumerate(data): 
        print (index+1, question['question']) 
        print ("A:"+ question['A']) 
        print ("B:"+ question['B']) 
        print ("C:"+ question['C']) 
        print ("D:"+ question['D']) 
        # print ('\n') 
      
        answers=input('Enter your answer')
        if answers.isalpha():
        # print ('\n') 

          if question['answer'] == answers:
             answersList += 1
             print ("Correct Answer")
          else:
             print ("Incorrect answer.The correct answer is " + question['answer'])
             print ('\n') 
        else:
            print ("Invalid input.Please input A,B,C or D")


    
    print("You got {} answers right".format(answersList))

    finish=time.time()
    # if finish-start>20
    
    # for element in range(len(data)):
    #     for key,value in data[element].items():
    #         print (key[0])

 
         
    # for element in data['one']:      #     for inner_element in element['number']: 
     #         print ("Question" + (inner_element) +":") 
     #     for elements in element['A']: 
    #       print ("A" + (elements)) 
read_file() 
 






 