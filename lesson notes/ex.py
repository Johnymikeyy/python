x = ["ab", "cd"]

for i in x:
    i.upper()
print(x)

i = 1

while True:
    if i % 3 == 0:
        break
    print(i)
    
    i += 1
    
tip = (1,2,3)

print(tip[1])

x = "abcd"

for i in range(len(x)):
    print(i)

x = "abcd"

for i in range(len(x)):
    x = "a"
    print(x)    
