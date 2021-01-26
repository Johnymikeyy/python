city = "I love Paris!"

def my_function(): 
    city = "I love London!"
    print(city) 
    
 

x = 10
def my_function_1(): 
    x = 20 
    print(x)
my_function_1() 



variable = "global"

def func_outer():
    variable = "enclosing outer local"
    def func_inner():
        variable = "enclosing inner local"
        def func_local():
            variable = "local"
            print(variable)
        func_local()
    func_inner()
 
func_outer()  # prints 'local' defined in the innermost function
print(variable)  # 'global' level variable holds its value



def func_enclosing1():
    x = 'outer variable'
    def func_enclosing2():
        x = 'inner variable'
        print("inner:", x)
    func_enclosing2()
    print("outer:", x)

func_enclosing1() 




def enclosing_func1():
    x = 'outer variable'
    def enclosing_func2():
        nonlocal x  # its inner-value can be used in the outer scope
        x = 'inner variable'
        print("inner:", x)
    enclosing_func2()
    print("outer:", x)

enclosing_func1() 


def outer():
    x = "previous"
    
    def inner():
        nonlocal x 
        x = "later"
        print("inner:", x)
    
    inner()
    print("outer:", x)