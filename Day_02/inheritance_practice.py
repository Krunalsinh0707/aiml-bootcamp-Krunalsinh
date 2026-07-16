class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, Welcome To Codetrade."
    
    

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        self.marks = []
    
    def greet(self):
        return "Hello Student Welcome to Codetrade."

    def __str__(self):
        return self.greet()


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return self.greet()
s1=Student("Krunal",101)
t1=Teacher("Yuvraj", "Maths")

print(s1)
print(t1)