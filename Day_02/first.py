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


s=Student("John", 101)

s.add_mark(85)

print(s.average())  # Output: 85.0