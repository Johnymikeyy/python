#if for the first one, elif for the rest, else the things you did not catch.
number1 = int(input("enter a number:"))
number2 = int(input("enter a number:"))
number3 = int(input("enter a number:"))
if (number1 > number2) and (number1 > number3):
    larger = number1
elif (number2 > number1) and (number2 > number3):
    larger = number2
else:
    larger = number3
print(larger)


number = int(input("enter a number:"))
if number == 0:
    print('0')
elif number < 0:
    print("negative number")
else:
    print("positive number")

