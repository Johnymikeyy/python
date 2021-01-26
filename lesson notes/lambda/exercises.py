def modular_function(n):
    return lambda x: x ** n

power_of_3 = modular_function(3)
print(power_of_3(5))

#####
mean = lambda x, y: (x+y)/2
print(mean(8, 10))

###
multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))

###
number_list = [1, 2, 3, 4]
result = map(lambda x:x**3, number_list)
print(list(result)) 

###
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
divisible_list = filter(lambda x:x%3==0, number_list) 
print(list(divisible_list))

####
number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result= list(filter(lambda x :x % 2 == 1, number_list))  
print(result) 