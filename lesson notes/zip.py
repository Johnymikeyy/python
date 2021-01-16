text = ["one", "two", "three", "four", "five"]
numbers = [1, 2, 3, 4, 5]

for x, y in zip(text, numbers):
    print(x, ":", y)
    
print(*zip(text, numbers))

print(list(zip(text, numbers)))


      

    
