### Fromkeys() method

data = ["a", "b", True, (False, 1), {"1" : 1}, [1,2], \
        {"2" : 2}, {2, 3}, "c", 23, 0]

types = ["int", "str", "bool", "list", "tuple", "dict", "set"]

total ={}.fromkeys(types, 0)#method of dictionary --- second parametres value-0