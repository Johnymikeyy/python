def multiply(mylist):
    mult = 1
    for x in mylist:
        mult *= x
    return mult
list1 = [3, 5, 6]

print(multiply(list1))