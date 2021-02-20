### 1 ### 
# Create a file and write string data in it. Name your file new_file.txt  

with open("new_file.txt", 'w', encoding="utf-8") as my_file:  
# create and open the file

    my_file.write('Hello Richard. This is my file.')  
    # write str data into the file
    
### 2 ###
# Let's write them to a file (new_file.txt) each on separate lines one after another.

colors = ['red\n', 'green\n', 'yellow\n', 'white\n', 'black\n']

with open("new_file.txt", "w", encoding="utf=8") as file:
    file.writelines(colors)  # writes each of the elements in a separate line

### 3 ###

# Keep the existing content of the file and add "blue" to the end of it.

colors = ['red', 'green', 'yellow', 'white', 'black']

with open("new_file.txt", 'w', encoding="utf-8") as file:
    for i in colors:
        file.write(i + '\n')  # we create "new_file.txt" for you 
        
with open("new_file.txt", "a", encoding = "utf = 8") as file:
    file.write("blue\n")  # add "blue" to the end of the text