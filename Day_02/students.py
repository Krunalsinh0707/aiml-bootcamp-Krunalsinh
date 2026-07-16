class Student:
        
    def __init__(self, name, roll,marks=None):
        self.name = name
        self.roll = roll
        self.marks=[]

    def add_mark(self,score):
        self.marks.append(score)
    

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks)/len(self.marks)
    

    def __str__(self):
        return f"Student Name: {self.name}, Roll Number: {self.roll}, Marks: {self.marks}, Average: {self.average()}"

    # def __repr__(self):
        # return f"Student('{self.name}', {self.roll}, {self.marks})"
    

s1=Student("Krunal",101)
s2=Student("Yuvraj",102)
s3=Student("Rahul",103)

s1.add_mark(85)
s1.add_mark(70)
s2.add_mark(90)
s2.add_mark(60)
s3.add_mark(95)
s3.add_mark(70)

students = [s1, s2, s3]

# print(f"Average marks of {s1.name} is: {s1.average()}")
# print(f"Average marks of {s2.name} is: {s2.average()}")
# print(f"Average marks of {s3.name} is: {s3.average()}")

# print(s1)   #<__main__.Student object at 0x0000025B28E3EF50>
print(s1)   #while printing single object it will call __str__ method and print the string representation of the object
print(students)     #while printing list of objects it will call __repr__ method and print the string representation of the object