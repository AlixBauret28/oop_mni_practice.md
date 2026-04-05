class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f"{self.name}, {self.age} years, {self.gender}"
