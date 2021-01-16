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


sentence = input("Give me a sentence:")

words = sentence.split()
longest = 0
i = 0
while i < len(words):
    if len(words[i]) > longest:
        longest = len(words[])
        i += 1
print("The length of the longest word is: ", longest)