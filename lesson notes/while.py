age = input("enter your age:")

while not age.isdigit():
  print("You entered incorrectly")
  age = input("enter your age again please:")
print("Great! You entered valid input, your age:", age)


answer = 27
question ="What a two-digit number am I thinking of?" 
print("Let's play a game!")

while True:
  guess = int(input(question))
  if guess < answer:
    print("Little higher!")
  elif guess >  answer:
    print("Little lower!")
  else:
    print("Are you a mind reader!")
    break
      

