### Underscore placeholders

no1 = 10_000_000_000
no2 = 100_000_000

addition = no1 + no2
print(addition)
print("{:,}".format(addition))

###
a, _, c, _ = (10, 20, 30, 40)

###
x, y, *_ = (11, 22, 33, 44, 55)

###
x, y, *z, t = (11, 22, 33, 44, 55, 66)