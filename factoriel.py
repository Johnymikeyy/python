def factoriel(a):
    if a == 0:
        return 1
    else:
        return a * factoriel(a-1)
a = int(input('enter a number:'))

print(factoriel(a))