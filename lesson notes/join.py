word = "gamer"    
for i in word.split():
    print("/".join(word)) 
    

a = ["world", "jupiter", "uranus"]
"-".join(["world", "jupiter", "uranus"])

print(a)

user = {"name": "Daniel", "surname": "Smith", "age": 25}

for attribute in user:
    print(attribute)
    
for i in user.items():
    print(i, end = "-" + '\n')
    
    
for key, value in user.items():
    print(key, ":", value)