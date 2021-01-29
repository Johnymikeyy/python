#sentence = input("Write me a sentence:")
sentence = "I am going to school"
words = sentence.split()
print(words)
print(*words)
print(list(words))
nested_list =[words]

print(nested_list)


longest = 0
i = 0
while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[i])
    i += 1
    
print("The lenght of the longest word is:", longest)
        