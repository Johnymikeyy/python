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


evens_count = 0
odds_count = 0
list_num = [11, 2, 24, 61, 48, 33, 3]

for i in list_num:
    if not i % 2:
        evens_count += 1
    else:
        odds_count += 1
print("The number of even numbers :", evens_count)
print("The number of even numbers :",odds_count)
    
for i in range(1, 10):
    print(str(i) * i)

a = 0
for i in range(1, 75):
    a += i
print(a)
    


   