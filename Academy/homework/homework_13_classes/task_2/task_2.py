# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
import doctest

class Dog:
    age_factor: int = 7
    def __init__(self, dog_name:str, dog_age:int) -> None:
        """
                Initials parameters:
                :param dog_name: str
                :param dog_age: int
                >>> Dog('jon', 3).dog_name
                'Jon'
                >>> Dog('jon', 3).dog_age
                3
                """
        self.dog_name: str = dog_name.capitalize()
        self.dog_age: int = dog_age

    def human_age(self) -> int:
        """
                Returns the age of the dog as a human
                :return: int
                >>> Dog('jon', 3).human_age()
                21
                """
        return self.dog_age * self.age_factor

if __name__ == '__main__':
    wild = Dog('wild', 5)
    print(f'I have a dog. His name is {wild.dog_name} and he is {wild.dog_age} years old.')
    print(f"{wild.dog_name}'s age in human equivalent is {wild.human_age()} years.")
    doctest.testmod()