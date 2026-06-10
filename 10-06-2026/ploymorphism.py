# Polymorphism

# In Python , ploymorphism allow the same method name to perform diffrent task depending on the object or situation.

# Two Types

#1. Method Overloading
#2. Method Overriding

# Method overloading mean creating multiple method with same name but diffrent parameter.

# Python do not support traditional method overloading directly, but it can be achived using default parameters.

class Calculator:

    def add(self , a , b = 0 , c = 0):
        return a + b + c

obj = Calculator()

print(obj.add(10 , 20))
print(obj.add(10 , 20 , 30))

# 2. Method Overriding

#Method Overriding occurs when a child class provides a diffrent implementation of a method already defined in the parent class

class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):

    def sound(self):
        print("Dog Sound")

obj = Dog()

obj.sound()

# Dog class overrides the sound() method of Animal class. Child class Method is executed insted of parent method.

# issubclass()

# issubclass() is built-in Python function used to check whether one class is a subclass of another class.

# syntax

# issubclass(child_class , parent_class)
# Return True or False

class Animal():
    pass

class Dog(Animal):
    pass

print(issubclass(Dog , Animal))
print(issubclass(Animal , Dog))

# super() keyword

# super() is used to call method or constructor of the parent class in the child class.

# It helps in reusing parent class code.

class Person:

    def __init__(self , name):
        self.name = name

class Student(Person):

    def __init__(self , name , marks):

        super().__init__(name)
        
        self.marks = marks

    def display(self):
        print("Name : " , self.name)
        print("Marks : " , self.marks)

obj = Student("Rahul" , 85)

obj.display()

#1.  Using super() with constructor

class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):

        super().__init__()

        print("Child Constructor")

obj = Child()

# 2. Access Parent class Method

class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Sound.")

obj = Dog()

obj.sound()

#3. Parent class and child class both have variables

class Person:

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

class Student(Person):

    def __init__(self , name , marks):

        super().__init__(name , marks)

    def display(self):
        print("Name :" , self.name)
        print("Marks : " , self.marks)

obj = Student("Zeel" , 78)

obj.display()
obj.display()





