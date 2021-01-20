def add(x, y):
    return(x+y)
print(add(5, 6))

print(type(add(5, 6)))

def calculator(a, b, opr):
    if opr == "+":
        return(a+b)
    elif opr == "-":
        return(a-b)
    elif opr == "*":
        return(a*b)
    elif opr == "/":
        return(a/b)
    else:
        return("please enter valid argument")
print(calculator(5, 9, "*"))

#abs and doc!
def absolute_value(num):
    return(abs(num))
print(absolute_value(-5))
print(abs.__doc__)

def my_function(a, b):
    print(a * b)
    area = a * b
my_function(3, 4)