for x in [1, 2, 3, 4]:
    print(x, ":", (lambda y : "odd" if y % 2 != 0 else "even")(x))
    
#(lambda statement)(argument)

print((lambda x, y: (x + y) / 2)(3, 5))

average = lambda x, y: (x + y) / 2
print(average (3, 5))

reverse = lambda a: a[::-1]
print(reverse("clarusway"))


#####
echo_word = lambda x, n : x * n
print(echo_word("hello", 3))

#########
number_list = [1, 2, 3, 4, 5]

result = list(map(lambda x : x*3, number_list))

print(result)