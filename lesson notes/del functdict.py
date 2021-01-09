family_name = { 'name1' : 'charlie', 
               'name2': 'george', 
               'name3': 'curly'
               }

print(family_name)
family_name.update({'name4': 'random'})
print(family_name)

del family_name['name1'], family_name['name2'] family_name['name3']  #deletes the item of dicttonary
print(family_name)

family_name.update({'name5':'new'})
print(family_name)