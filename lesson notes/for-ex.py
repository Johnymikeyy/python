number = int(input("enter a number:"))

for i in range(number):
    result = number * i
    print(f"{number} * {i}", "=", result)
    
    
for i in range(11):
    print(i, end="+")
    
print(*range(5, 25, 2))