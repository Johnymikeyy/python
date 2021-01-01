def cube_c(x):
    return 12 * x
def cube_a(x):
    return 6 * x ** 2
def cube_v(x):
    return x ** 3

x = int(input('enter the distance of the edge:'))

print(f" the edge {x}, circumference of the cube {cube_c(x)}, area of the cube {cube_a(x)}, volume of the cube {cube_v(x)} ")