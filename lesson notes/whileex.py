sentence = str(input("Sentence:"))
list = sentence.split(" ")
index = 0
longest = ""
while index < len(list):
    if len(list[index]) > len(longest):
        longest = list[index]
    index += 1
print(sentence)
print("length of the longest word is:", int(len(longest)))


