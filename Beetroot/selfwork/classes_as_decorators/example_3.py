def auto_str_class(any_class):
    def str_(self):
        variables = (f'{key}={value!r}' for key, value in vars(self).items())
        return f'{any_class.__name__}({", ".join(variables)})'

    any_class.__str__ = str_
    return any_class

@auto_str_class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Jane', 26)
print(p)