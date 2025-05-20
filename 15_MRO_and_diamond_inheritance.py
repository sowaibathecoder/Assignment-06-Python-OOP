"""
Question: 15 {Method Resolution Order (MRO) and Diamond Inheritance}
Assignment:
Create four classes:

A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
"""


class A:
    def show(self):
        print("A parent class")

class B(A):
    def show(self):
        print("B override A")

class C(A):
    def show(self):
        print("C also override A")

class D(B, C):
    pass

d = D()
d.show()
