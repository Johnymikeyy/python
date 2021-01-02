name = 'john' # global parametres
age = 36

def hello():
    name = 'ali'   # local parametres in fuctions !!!
    age = 20
    return f'my name is {name} and i am {age} years old'
   
print(hello())
print(name)

################

x = 'global'

def myfunc():
    x = 'local'
    return x

print(x)
print(myfunc())

##################

x = 'global level'

def func():
    x = 'func level'
    def innerfunc():
        x = 'local level'
        print(x)
    innerfunc()

func()

    
