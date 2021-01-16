names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]

for name in names:
    print("Hello", name)
 
#append method
number_list = []    
for i in range(1, 6):
    number_list.append(i)
print(number_list)


word = "Clarus"
count = 0
for i in word:
    count += 1
    if count < len(word):
        i = i + "-"
    print(i, end = "")
 
    
   