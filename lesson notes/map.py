#map(function, iterable) returns a list of the outputs
# such as list, tuple

iterable = [1, 2, 3, 4, 5]

result = map(lambda x : x ** 2, iterable)

print(result)
print(list(result))
print(* result)

for i in result:
    print(i)
    print(list(result))
 


#####
def square(x):
    return x**2
iterable = [1, 2, 3, 4, 5]  
result = map(square, iterable)
print(list(result))
 
 
#####   
letter1 = ["o", "s", "t", "t"]
letter2 = ["n", "i", "e", "w"]
letter3 = ["e", "x", "n", "o"]
numbers = map(lambda x,y,z: x+y+z, letter1, letter2, letter3)

print(list(numbers))



#####
nums1 = [9, 6, 7, 4]
nums2 = [3, 6, 5, 8]

total = map(lambda x, y : (x + y) / 2, nums1, nums2)
print(list(total))

#####
words1 = ["you", "much", "hard"]
words2 = ["I", "you", "he"]
words3 = ["love", "ate", "works"]

sentence = map(lambda a, b, c: b+ " " + c + " "+ a , words1, words2, words3)
print(*list(sentence))
seperate = list(sentence)
for i in seperate:
    print(i)
    
    


    
