# class

class Dog:

    def __init__(self,name,age):
         self.name=name #Attribute
         self.age=age

    def bark(self):
         return "Woof!"
    
my_dog=Dog("Kiity",12)
print(my_dog.name)
print(my_dog.bark())

#encapsulation

class Bank_Account:
     
     def  __init__(self,balance):
           self.__balance=balance #private attribute

     def deposit(self,amount):
          if amount >0:
               self.__balance += amount
    
     def get_balance(self):
          return self.__balance
     
account=Bank_Account(100000)
account.deposit(500)
print(account.get_balance())
#print(account.__balance)

#inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

# Create objects of subclasses
cat = Cat()
dog = Dog()

print(cat.speak())  # Output: Meow
print(dog.speak())  # Output: Woof

#polymorphism
class Bird:
    def fly(self):
        return "Flies in the sky"

class Airplane:
    def fly(self):
        return "Flies through the air"

def let_it_fly(flyable):
    print(flyable.fly())

bird = Bird()
plane = Airplane()

let_it_fly(bird)   # Output: Flies in the sky
let_it_fly(plane)  # Output: Flies through the air
