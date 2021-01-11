given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]

print(set(given_list))

capital1 = "washington"
capital2 = "wellington"

print(set(capital1).intersection(set(capital2)))
print(set(capital1).union(set(capital2)))
print(set(capital1).difference(set(capital2)))

set1 = "TWELVE PLUS ONE"
set2 = "ELEVEN PLUS TWO"

if set(set1) == set(set2):
    print("we are the same")
 
   
word = input("enter yes or no:")
if word == "yes":
    print("you are entered True")
else:
    print(False)

print("you entered", word == "yes")

status = input("Enter Yes or No:").title().strip() == "Yes"
print("You entered", status)

number = int(input("enter a number:"))
if number % 2 == 0:
    print("The {} is even".format(number))
else:
    print("The {} is odd".format(number))
    

number = int(input("enter a number:"))
if number < 0:
    print("The {} is negative".format(number))
else:
    print("The {} is positive".format(number))
    
    
number1 = float(input("enter a number:"))
number2 = float(input("enter a number:"))

if number1 < number2:
    print("The large number is {}".format(number2))
else:
    print("The large number is {}".format(number1))

bool_value = False    
if bool_value:
    print("Yes")
else:
    print("No")

