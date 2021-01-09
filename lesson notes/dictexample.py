family_name = { 'name1' : 'charlie', 
               'name2': 'george', 
               'name3': 'curly'
               }

print(family_name)
family_name.update({'name4': 'random'}) #update the dictionary

print(family_name)

family_name['name4'] = 'dsfdsf'
print(family_name)

print(family_name['name1'])


dict2 = dict(animal = 'dog', planet = 'world', number = 40)
print(dict2) #converts


family_name1 = dict(name1 = 'charlie', 
               name2 = 'george', 
               name3 = 'curly') 
print(family_name1)     
print(family_name)

print(family_name.items())
print(family_name.keys())
print(family_name.values())

print(list(family_name.items()))
print(list(family_name.keys()))
print(list(family_name.values()))