"""
Question: 07 {Access Modifiers: Public, Private, and Protected}
Assignment:
Create a class Employee with:

* a public variable name,
* a protected variable _salary, and
* a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
"""

class Employee:
    def __init__(self):
        self.name = "Sowaiba Naz"
        self._salary = "$5,00,000"
        self.__ssn = "123-45-678"

e = Employee() # object created
print(e.name)
print(e._salary)
# print(e.__ssn) # ❌ Error
print(e._Employee__ssn)  # ✅ Accessing private using name mangling