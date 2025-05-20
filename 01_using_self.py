"""
Question: 01 {Using self}
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to
initialize these values via a constructor. Add a method display() that prints 
student details.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"\nName: {self.name}, Marks: {self.marks}")
        print(f"\nMy name is {self.name}, and my marks are in my python quiz is 100 out of {self.marks}.\n")


# Object banayein
student1 = Student("Sowaiba Naz", "99")
student2 = Student("Hina", "85")
student1.display()
student2.display()

print(student1.name, student1.marks) # seperately print name nad marks