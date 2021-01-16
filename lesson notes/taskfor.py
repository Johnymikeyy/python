print(*range(10, 0, -2))

for i in range(10, 0, -2):
    print(i, "-")
    
    
evens = []
odds = []

for i in range(10):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
        
print(evens)
print(odds)
   