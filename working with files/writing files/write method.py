with open("dummy_file.txt", 'w', encoding="utf-8") as file:  
# we create and open the file

    file.write('This is the first line of my text file')  
    # writes str data into file

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the 'dummy_file'
    
    
#output
This is the new line for my dummy_file

#####

with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())
    
#output

My first sentenceMy second sentence,My third sentence
My fourth sentence My last sentence

###########

fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    for basket in fruits:
        file.write(basket + '\n')  # adds a newline character to each string
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())  # reads and displays entire lines in a list
    
#output

Banana
Orange
Apple
Strawberry
Cherry

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']


####Using with ... as ... block, create a file and write the following string data in it. Name your file new_file.txt

with open("new_file.txt", "w", encoding="utf=8") as file:  
# create and open the file

    file.write('Live to help others live.')  
    # write str data into the file
