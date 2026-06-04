# 1. Class and Object
# Example 1
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Ram", 22)
# s1.display()
# Example 2
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def show(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)


# c1 = Car("BMW", "Black")
# c1.show()
# Example 3
# class Employee:
#     def __init__(self, emp_id, salary):
#         self.emp_id = emp_id
#         self.salary = salary

#     def display(self):
#         print("Employee ID:", self.emp_id)
#         print("Salary:", self.salary)


# e1 = Employee(101, 25000)
# e1.display()
# Example 4
# class Mobile:
#     def __init__(self, company, price):
#         self.company = company
#         self.price = price

#     def details(self):
#         print("Company:", self.company)
#         print("Price:", self.price)


# m1 = Mobile("Samsung", 20000)
# m1.details()
# 2. Inheritance
# Example 1: Single Inheritance
# class Parent:
#     def show_parent(self):
#         print("This is Parent class")


# class Child(Parent):
#     def show_child(self):
#         print("This is Child class")


# obj = Child()
# obj.show_parent()
# obj.show_child()
# Example 2: Multilevel Inheritance
# class A:
#     def show_a(self):
#         print("Class A")


# class B(A):
#     def show_b(self):
#         print("Class B")


# class C(B):
#     def show_c(self):
#         print("Class C")


# obj = C()
# obj.show_a()
# obj.show_b()
# obj.show_c()
# Example 3: Hierarchical Inheritance
# class A:
#     def show_a(self):
#         print("Class A")


# class B(A):
#     def show_b(self):
#         print("Class B")


# class C(A):
#     def show_c(self):
#         print("Class C")


# obj1 = B()
# obj2 = C()

# obj1.show_a()
# obj1.show_b()

# obj2.show_a()
# obj2.show_c()
# Example 4: Hybrid Inheritance
# class A:
#     def show_a(self):
#         print("Class A")


# class B(A):
#     def show_b(self):
#         print("Class B")


# class C(A):
#     def show_c(self):
#         print("Class C")


# class D(B, C):
#     def show_d(self):
#         print("Class D")


# obj = D()
# obj.show_a()
# obj.show_b()
# obj.show_c()
# obj.show_d()
# 3. Encapsulation
# Example 1
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance


# acc = BankAccount(5000)
# acc.deposit(2000)

# print("Current Balance:", acc.get_balance())
# Example 2
# class Student:
#     def __init__(self, marks):
#         self.__marks = marks

#     def set_marks(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks


# s1 = Student(85)
# s1.set_marks(90)

# print("Marks:", s1.get_marks())
# Example 3
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def increase_salary(self, amount):
#         self.__salary += amount

#     def get_salary(self):
#         return self.__salary


# emp = Employee(30000)
# emp.increase_salary(5000)

# print("Salary:", emp.get_salary())
# Example 4
# class ATM:
#     def __init__(self, pin):
#         self.__pin = pin

#     def change_pin(self, new_pin):
#         self.__pin = new_pin

#     def get_pin(self):
#         return self.__pin


# atm = ATM(1234)
# atm.change_pin(5678)

# print("New PIN:", atm.get_pin())

# Important correction: in Python constructor must be written as:

 