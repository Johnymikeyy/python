word = input("Enter a word:")
seperator = input("Enter a seperator:")
repetition = int(input("How many times you want it to repeat:"))

print(word * repetition, sep = "f{seperator}")