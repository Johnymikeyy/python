class student:
    
    school_name = 'x high school' # for common 
    numer_of_students = 0
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        student.numer_of_students += 1
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def schoolname(self):
        return f'name of the school {self.school_name}'
    
    
print(student.numer_of_students)

student_1 = student('hale', '22', [25, 69, 89, 22])  # name, age instance parametres
student_2 = student('charlote', '25', [18, 98, 56, 78])  # student_2 instance


print(student.numer_of_students)

print(student_1.average())
print(student_2.average())

print(student_1.name)
student_1.name = 'chloe'
print(student_1.name)

print(student_1.school_name)
print(student.school_name)

print(student_1.schoolname())
print(student_2.schoolname())

print(student_1.__dict__)
print(student.__dict__)





