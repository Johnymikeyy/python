#we can do the closing process with the close() method, 
#but there is a slightly easier way to do this. 
#Using the with .... as ... block. In fact, 
#the actual use of the with ... as ... block is to make sure that all the necessary functions are called. 

with open("fishes.txt", "r") as sea:
    print(sea.read())  # needs indented code block
    
#output

Orca is a kind of Dolphin.
Blue Whale is the largest animal known on earth.
Sharks are the sister group to the Rays (batoids).
The Tuna Fish can weigh up to 260 kg.
Squid and Octopus are in the same class.


###
with open("fishes.txt", "r") as my_file:
    print(my_file.read())