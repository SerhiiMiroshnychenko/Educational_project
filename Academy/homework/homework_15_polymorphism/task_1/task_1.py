"""Method overloading.
Create a base class named Animal with a method called talk
and then create two subclasses: Dog and Cat, and make their
own implementation of the method talk be different. For instance,
Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance
 of a Cat or Dog classes and performs talk method on input parameter.  """
#%%
class Animal:
    animal_type = 'unknown'
    def __new__(cls, name):
        print(f'The animal type {cls.animal_type} was born. It was named {name}.')
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'The {self.animal_type} named {self.name} died.')

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method.')

#%%
class Dog(Animal):
    animal_type = 'dog'
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f'The {self.animal_type} named {self.name} say: "Woof-woof!"')

#%%
class Cat(Animal):

    animal_type = 'cat'
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f'The {self.animal_type} named {self.name} say: "Meow!!"')

if __name__ == '__main__':
    dog = Dog('White')
    dog.talk()
    cat = Cat('Bond')
    cat.talk()
