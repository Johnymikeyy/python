a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

print("{}*{}*{} = ".format(a, b, c), a*b*c)

height = int(input("enter your height:"))
weight = int(input("enter your weight:"))

print("body mass index:", weight / height ** 2)

money = 200
piece = 11
print("I can buy", int(money/piece), "pieces")
print("I have", money % piece+"$")

