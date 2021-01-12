#1
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

print("{}*{}*{} = ".format(a, b, c), a*b*c)

#2
height = int(input("enter your height:"))
weight = int(input("enter your weight:"))

print("body mass index:", weight / height ** 2)

#3
money = 200
piece = 11
print("I can buy", int(money/piece), "pieces.")
print("Now, I have", money % piece,"$")

#4
number1 = int(input("enter a number:"))
number2 = int(input("enter a number:"))

apples = number1
computers = number2 
number1 = number2
print(apples, computers)

#5
#print((x-y)*(x+y))

#6
word = input("Enter a word:")
seperator = input("Enter a seperator:")
repetition = input("How many times you want it to repeat:")

print(word * repetition, sep = "+")
      
      

