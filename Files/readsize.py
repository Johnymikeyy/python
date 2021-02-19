sea = open("fishes.txt", 'r')   

print(sea.read())  # displays the entire text content

sea.close()  # be sure to close the file

#output

Orca is a kind of Dolphin.
Blue Whale is the largest animal known on earth.
Sharks are the sister group to the Rays (batoids).
The Tuna Fish can weigh up to 260 kg.
Squid and Octopus are in the same class.



####
sea = open("fishes.txt", 'r')   

print(sea.read(33))  # displays the first 33 chars of the text
print()
print(sea.read(25))  # displays the next 25 chars of the text
print()
sea.seek(0)  # changes the stream (cursor) position to zero
print(sea.read(33))  # displays the first 33 chars again
print()
print(sea.tell())  # returns the current stream (cursor) position

sea.close()

#output

Orca is a kind of Dolphin.
Blue W

hale is the largest anima

Orca is a kind of Dolphin.
Blue W

34