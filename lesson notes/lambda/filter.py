#with lambda function that tests each element in the sequence 
# True or not
#filter(funcion, sequence)

first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x: x % 2 == 0, first_ten)

print(list(even))

#task
words = ["apple", "swim", "clock", "me", "kiwi", "banana"]

five_letter = filter(lambda a: len(a)<5, words)

for i in five_letter:
    print(i)


#task2
vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vowels = filter(lambda x: True if x in vowel_list else False, first_ten)
print(list(vowels))


######
def modular_function(n):
    return lambda x: x ** n

pow2 = modular_function(2)
pow3 = modular_function(3)

print(pow2(3))


#task3

def repeater(n):
    return lambda x: x * n

print("ali " * 4)
two_times = repeater(2)
print(two_times("ali "))

#task4

def functioner(n):
    return lambda x: print(x, n)

myprint_smile = functioner(":)")
myprint_sad = functioner(":(")
myprint_neutral= functioner(":I")

myprint_smile("hello")
myprint_sad("noo")
myprint_neutral("yess")


####
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x : x > 5 , number_list))
print(result)

