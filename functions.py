# rather than writing the second time, we call the functions

def func():                # def is key, func is the name of functions
    print('hi everyone')
    
func()

def my_func(username = 'christine'):     #username is parametre
    print(f"hi {username}")
    
my_func('john')   # john is argument
my_func('kim')

my_func()


def function(username, age=25):
    print(f'hi {username}, you are {age} years old')
    
function('john', 36)



def func1():
    return 7 + 8    # we did not define what it will do ! return???
def func2():
    print(2 + 8)    # we defined what it will do ----print!
    
func1()
func2()

result1 = func1()
result2 = func2()

print(f'first 1, {result1}')
print(f'second 2, {result2}')  # gives None

def func():   # if I want it not to make a process
    pass

func()
