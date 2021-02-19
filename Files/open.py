#The encoding parameter indicates the encoding that needs to be used to decode or encode a file. The default value depends on the platform you use and its language. UTF-8 is one of the most preferred used encodings, and Python generally defaults to using it. UTF stands for “Unicode Transformation Format”, and the ‘8’ means that 8-bit values are used in the encoding. 
#We can open a file in the same way by using the following syntax :

my_file = open("first_file.txt", encoding="utf-8")
# we've used 'utf8' encoding format just the same as the previous one

#you have a text file (fishes.txt) stored in the current working directory. Open this file and assign it to my_file. Then print the type of my_file.

my_file = open("fishes.txt", encoding="utf-8") 

print(type(my_file))