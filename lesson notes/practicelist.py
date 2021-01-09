city = ['addis baba', 'rome', 'tokyo', 'istanbul']

print(sorted(city)) #sorts alphabetical

city.sort()
print(city)


#sort the list according to their lenght

print(sorted(city, key=len, reverse=True))

city.sort(key=len, reverse=True)
print(city)
