def motto():
    print("do not hesitate to reinvent yourself")
motto()

def add(x, y):
    print(x+y)
add(5, 6)

def calculator(a, b, c):
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    else:
        print("please enter valid argument")
calculator(5, 7, "*")


def add(x, y):
    return(x+y)
print(add(5, 6))