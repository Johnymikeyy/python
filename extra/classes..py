# car is object and it has methods (in functions)

class car:
    def __init__(self, brand, model, year): #starts the attribiutes
        self.brand = brand
        self.model = model    # shows the features when it is created
        self.year = year
    
    def brandmodel(self):
        return f'brand of the car {self.brand} and the model is {self.model}'
         
car_1 = car('bmw', 'i5', 2020)
car_2 = car('mercedes', 'a4', 2019)

#car_1.brand = 'bmw'
#car_1.model = 'a4'
#car_1.year = 2020

#car_2.brand = 'mercedes'
#car_2.model = 'i5'
#car_2.year = 2019

print(car_1) 
print(car_1.brand)

print(car_1.brandmodel())

####################

class movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director
        
movie_1 = movie('eyes wide shut', 'kubrick')
movie_2 = movie('interstellar', 'jolan')

print(movie_1.director)
print(movie_2.name)