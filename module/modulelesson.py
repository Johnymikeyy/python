#Built_in Modules

import math 

print(math.pi)
print(math.factorial(4))
print(math.log10(1000))

from math import pi, factorial, log10 # second solution

#task

from string import punctuation, digits

print(punctuation)
print(digits)

#task

import datetime
print(datetime.date.today())
print(datetime.datetime.now())

#task

from datetime import date
birth = date(571, 4, 22)
death = date(632, 6, 8)

print(death - birth)
live_days = date.toordinal(death) - date.toordinal(birth)
print(live_days)

#task

import random
city = ["Stockholm",  "Istanbul", "Seul", "Cape Town"]
print(random.choice(city))

from random import choice
print(choice(city))

