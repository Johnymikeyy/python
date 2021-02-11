### Enumerate
birds = ["nightingale", "phonenix", "sparrow", "eagle"]

index = 0

for bird in birds:
    print(index, bird)
    index += 1

###
for index, bird in enumerate(birds):
    print(index, bird)
    
print(*enumerate(birds))