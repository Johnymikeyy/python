while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except:
        print("Something went wrong...Try again.")



#################################3333

while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two  # normal part of the program
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")  # executes when division by zero
    else:
        print("The result of the division is : ", division)  # executes if there is no exception
    finally:
        print("Thanks for using our mini divison calculator! Come again!")
        break  # exits the while loop
    
    
    #output 1
    
The first number please : 7
The second number please : 2
The result of the division is :  3.5
Thanks for using our mini divison calculator! Come again!


#output 2

The first number please : 7
The second number please : 0
You can't divide by zero! Try again.
Thanks for using our mini divison calculator! Come again!


######################333
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except Exception as e:
        print("Something went wrong...Try again.")
        print("Probably it is because of '{}' error".format(e))
        break
        
        
#output

The first number please : 4
The second number please : 0
Something went wrong...Try again.
Probably it is because of 'division by zero' error.


#################################3

try :
    a = 10
    b = 2
    print("The result of division is :", c)
except Exception as e:
    print("The error message is : ", e)
    
    
#output

The error message is :  name 'c' is not defined