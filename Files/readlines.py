# It reads the entire file line by line in the list form.

sea = open("fishes.txt", 'r')   

print(sea.readlines())

sea.close()

#output

# ['Orca is a kind of Dolphin.\n', 'Blue Whale is the largest animal known on 
# earth.\n', 'Sharks are the sister group to the Rays (batoids).\n', 'The Tuna 
# Fish can weigh up to 260 kg.\n', 'Squid and Octopus are in the same class.']