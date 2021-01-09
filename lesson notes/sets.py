set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
set_2 = set(colors)
print(set_1)

letter = "a b c d e f g h i j k l m n o p r s t u v y z".split()
print(letter)

print(set(letter))

letter1 = "f g h i j k l m n o p r s" 

numbers = "1,2,3,4,5"

set(letter) == set(letter1)

print(set(letter).difference(letter1)) #difference
print(set(letter) - set(letter1))

print(set(numbers).union(letter1)) #union
#print(a I b)

print(set(letter) & set(letter1)) #intersection

day = "09.01.2021"
daybyday = {"09/01/2021"}
print(set(day))
print(daybyday)

      