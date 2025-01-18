from functools import reduce

def sum(value1:int, value2):
    return value1 + value2

print(sum(1, 2))
# print(sum("hola", 2))


substract = lambda value1, value2 : value1 - value2
multiply_2 = lambda value1 : value1 * 2



my_lis = [1, 2, 3, 4, 5]
print(list(map(multiply_2,my_lis)))
print(list(map(lambda value1 : value1 * 2,my_lis)))
print(list(filter(lambda value1 : value1 % 2 == 0,my_lis)))
print(reduce(lambda value1, value2: value1 + value2,my_lis))


#lambdas con varias lineas



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__phone_number = "123456789"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_phone_number(self, phone_number):
        self.__phone_number ="34"+ phone_number

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

borja = Person("Borja", 25)
borja.__phone_number = "987654321"

class Contact:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f"Email: {self.email}"

class Student(Person,Contact):
    def __init__(self, name, age, email):
        Person.__init__(self, name, age)
        Contact.__init__(self, email)

    def __str__(self):
        return f"{Person.__str__(self)}, {Contact.__str__(self)}"

student = Student("Borja", 25, "borja@cole.com")
print(student)