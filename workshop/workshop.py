
max = a
if b > max:
   max = b
   print(max)
   
number = int(input('Please enter a number: '))
i = 0
while i in range(0, number):
    print(i**2)
    i += 1
    
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
   print(f"The type of {i} is {type(i)}")


