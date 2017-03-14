import json

def read_file():

    path ='H:\AndelaBootCampWk2\Masomo\Quiz1.json'
    json_data=open(path).read()

    data=json.loads(json_data)

    for index, question in enumerate(data):
        print (index+1, question['question'])
        print ("A:" +question['A'])
        print ("B:"+ question['B'])
        print ("C:"+ question['C'])
        print ("D:"+ question['D'])
        print ('\n')

        
    # for element in data['one']:
    #     for inner_element in element['number']:
    #         print ("Question" + (inner_element) +":")
    #     for elements in element['A']:
    #       print ("A" + (elements))
    

            

            


    
 
read_file()
