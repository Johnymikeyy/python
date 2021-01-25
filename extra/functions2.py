# built in functions / ready functions 

mylist = [1, 4, 9, 3, 7, 4]
print(len(mylist)) 

myset = set(mylist)
print(myset)

print(sum(myset))

#################

def func(x):
    return x**2
print(func(3))

y = lambda a: a**2   #  lambda 
print(y(7))

ampule = lambda b: b + 5 
print(ampule(10))

output = lambda a, b : a - b 
print(output(22, 15))
