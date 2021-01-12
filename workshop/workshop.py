sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for item in sample_list:
    #print(f"The type of {sample_list[]} is {type(sample_list[])}")


 word = input("Enter a word:")
 seperator = input("Enter a seperator:")
 repetition = input("How many times you want it to repeat:")

 print(*list([word] * int(repetition)), sep=seperator)