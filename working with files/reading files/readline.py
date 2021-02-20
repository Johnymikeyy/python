sea = open("fishes.txt", 'r')   

print(sea.readline())  # displays the first line of the text
print(sea.readline())  # displays the second line
print(sea.readline())  # each time it goes to the new line

sea.close()

#output

Orca is a kind of Dolphin.

Blue Whale is the largest animal known on earth.

Sharks are the sister group to the Rays (batoids).


######

sea = open("fishes.txt", 'r')   

print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))

sea.close()

# output

Orca is a kin
d of Dolphin.


Blue Whale is

#The output has two empty lines. 
# One of them is caused by the last character (\n) of the first line and the other is because of the default empty line that the .readline() method puts between each line.