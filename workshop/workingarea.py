#1 "Write a program that multiplies three numbers entered by the user. Print the output with the format method."
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))

print("{}*{}*{} = ".format(a, b, c), a*b*c)

#2 "Write a program that calculates body mass index from **height** and **weight** entered by the user.
height = int(input("enter your height:"))
weight = int(input("enter your weight:"))

print("body mass index:", weight / height ** 2)

#3 "With your $ 200, how many pieces of material can you get for $ 11 each? How much money do you have left after buying?"
money = 200
piece = 11
print("I can buy", int(money/piece), "pieces.")
print("Now, I have", money % piece,"$")

#4 "Ask the user for two numbers and assign these numbers to variables and replace the values of these variables with each other."
number1 = int(input("enter a number:"))
number2 = int(input("enter a number:"))

a = number1
b = number2 

print("Numbers\na= {} b= {}".format(a, b))
a, b = b, a
print("New numbers\na= {} b= {}".format(a, b))

#5 "Write a Python program to solve (x - y) * (x + y)."
x = 5 
y = 3
print((x-y)*(x+y))

#6 "Get **word**, **seperator** and **repetition** values from the user and print the word on the screen according to the given values.
word = input("Enter a word:")
seperator = input("Enter a seperator:")
repetition = input("How many times you want it to repeat:")

print(word * repetition, sep = "+")
      
#7 Get a sitring and an integer input from the user and get the output shown as in the example.
# "Ex: word = Clarusway n = 3 OUTPUT = waywayway"

word = input("enter a word :")
number = int(input("enter a number:"))

print(word[number - 3:])

#8 "Get a number from the user.
# "If the number is divided by 3 print *Clarus*, 
# "if it is divided by 5 print *way*, 
# "if it is divided by both 3 and 5 print *Clarusway*.
# "If not, print the number itself."

#9 "letters = \"abclarusxyz\
    # "- get the word **clarus**
    # "- get the word **cba**
    # "- print the last eight characters in reverse order"
    
#10 "Print **Clarusway is the best** from the elements of the rand_list list.
# "rand_list = [1,[1, 2, \"Clarus\", [2, \"way\"]], \" is the best\"]"

#11 "Sort the list given below in ascending order. Find the missing number from 1 to 10.
#   "num_list = [2, 3, 1, 5, 6, 4, 9, 8, 10]

#12 "Print the oldest person's name?
# "old ={\n",
# "  \"Emma\": 71,\n",
# "  \"Jack\": 45,\n",
# "  \"Amy\": 15,\n",
# "  \"Ben\": 29\n",

#13   "Write a Python program to sum all the items in a dictionary.
#     "my_dict = {'data1':100,'data2':-54,'data3':247}"

#14  "Write a Python program to compute average of two given lists.
# "nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
# "nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
