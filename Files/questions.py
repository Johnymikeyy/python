### 1 ### Open this file using the "utf-8" as the encoding parameter 
# and assign it to my_file. Then print the type of my_file.

my_file = open("fishes.txt", encoding = "utf-8") 

print(type(my_file))


### 2 ### Open this file for reading mode and assign it to my_file. 
###  And read the entire file at oncethen close the file.

my_file = open("fishes.txt", 'r')   

print(my_file.read()) 

my_file.close()



### 3 ### Open this file for reading mode and assign it to my_file. 
# And read the first 40 chars of the text then close the file.

my_file = open("fishes.txt", "r")   

print(my_file.read(40)) 

my_file.close()


### 4 ### Open this file and assign it to my_file. 
# And read the first line of the text then close the file.

my_file = open("fishes.txt", 'r')   

print(my_file.readline()) 

my_file.close()


### 5 ### Open this file and assign it to my_file. 
# And read the first 9 chars of the first line of the text then close the file.

my_file = open("fishes.txt", 'r')   

print(my_file.readline(9)) 

my_file.close()


### 6 ### Open this file and assign it to my_file. 
# And read the entire file line by line then close the file.

my_file = open("fishes.txt", 'r')   

print(my_file.readlines()) 

my_file.close()


### 7 ### Open this file and assign it to my_file. 
# And print entire file using for loop then close the file.

my_file = open("fishes.txt", 'r')   

for line in my_file:
    print(line)

my_file.close()

### 8 ### 