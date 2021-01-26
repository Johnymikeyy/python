def my_function(first, last) : 
    print('Your first name is :', first)
    print('Your last name is :', last)

my_function('Richard', 'Rice') 


x = 10
def my_function_1(): 
    x = 20 
    print(x)
    
print(x)



x = 10
def my_function():  # fix me!
    global x
    x += 5 
    print(x)
    
    
my_function()


count = 1

def counter():
    global count
    count += 1
    print(count)  

counter() 


def myfunc1():
  x = "hi"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())




x = 10
def my_function_1(): 
    x = 20 
    print(x)
my_function_1() 



x = 'My name is Richard'
def my_function_1(): 
    x = 'My name is John'
    
print(x)



