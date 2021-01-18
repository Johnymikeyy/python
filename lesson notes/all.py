#returns #True if all elements in an iterable are true
         #False if any element in an iterable is false

names = ["susan", "tom", "False"]   
mood = ["happy", "sad", 0]
empty = []  #---- gives True

print(all(names), all(mood), all(empty), sep = "\n")

#any function  
 #True if at least one element of an iterable is true
 #False if all elements are false or if an iterable is empty
 
listA = ["susan", "tom", "False"]  
listB = [None, (), 0]
empty = {}

print(any(listA), any(listB), any(empty), sep = "\n")

#filter(function, iterable)

listA = ["susan", "tom", False, 0, "0"]  

filtered_list = filter(None, listA)# None, it filters True ones

print("the filtered elements are:")
for i in filtered_list:
    print(i)
    
#enumerate(iterable, start = 0)
grocery = ["bread", "water", "olive"]
enum_grocery = enumerate(grocery)

print(type(enum_grocery))
print(list(enum_grocery))
enum_grocery = enumerate(grocery, 10)
print(list(enum_grocery))

#max, min
number = [-222, 0, 16, 5, 10, 6]
largest = max(number)
smallest = min(number)

print(largest)
print(smallest)

#sum
print(sum(number))
numbers = sum(number, 20)
print(numbers)

#round
print(round(12))
print(round(10.7))
print(round(3.665, 2))
print(round(3.675, 2))