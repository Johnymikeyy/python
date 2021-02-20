fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # creates a file containing the elements of the list

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the file

with open("fruits.txt", 'a', encoding="utf-8") as file:
    file.write('Melon\n')  # adds "Melon" to the end of the existing file
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the last content of the file

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())
    
#output

Banana
Orange
Apple
Strawberry
Cherry

Banana
Orange
Apple
Strawberry
Cherry
Melon

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n', 'Melon\n']