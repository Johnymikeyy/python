fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # takes an iterator for writing
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())
    
    
#output

Banana
Orange
Apple
Strawberry
Cherry

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']


#####
Think of that we have a list of colors. Let's write them to a file each on separate lines one after another.

colors = ['red', 'green', 'yellow', 'white', 'black']

with open("new_file.txt", 'w', encoding="utf=8") as file:
    for i in colors:
        file.writelines(i + "\n")  # adds a newline character