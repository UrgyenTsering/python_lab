
# 👉 Method overriding = Child class changes (redefines) a method of parent class
# Same method name
# Same parameters
# Different behavior

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):  # Child class
    def speak(self):  # Overriding
        print("Dog barks")
        
class Cat(Animal):
    def speak(self):
        print("Meow")


# Create object
a=Animal()
d = Dog()
c=Cat()
a.speak()
d.speak() # Dog class method (overrides)
c.speak() # Cat class method (overrides)

# OUTPUT: 
# Animal sound
# Dog barks
# Meow

# Even though Animal has speak(), the child version is used by d.speak() and c.speak. Python checks the object type first, not the parent





# 🔹 Using super() (Important 🔥)
# 👉 Sometimes you want to use parent method + add extra behavior

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()   # call parent method
        print("Dog barks")

d = Dog()
d.speak()

"""
  OUTPUT: 
  Animal sound
  Dog barks
   
"""
