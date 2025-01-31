### PROTECTED ATTRIBUTES
class Person:
    """
    Person class
    """

    # class attribute, can be accessed directly from outside the class
    # Person.class_attr
    class_attr = "Human being"

    def __init__(self, name):
        # protected instance attribute
        # can be accessed from outside the class but not recommended
        # Person().class_attr
        self._name = "protected!"

    # recommended way of using protected attribute
    # Person().get_protected_instance_attr
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        self._name = newname

joe = Person('Joe')
print(joe.name)
joe.name = 'John Doe'
print(f"after rename: {joe.name}")
print('---------------------------')

### PRIVATE ATTRIBUTES
class Car:

    def __init__(self, make):

        # private instance attribute
        # canNOT be accessed from outside the class
        # Car().__make will return AttributeError
        self.__make = make

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, newmake):
        self.__make = newmake

class Mustang(Car):
    pass

ford = Car("Ford")
print(ford._Car__make) # possible but not recommended
print(ford.make)
ford.make = 'Ford Mustang GT'
print(f"after rename: {ford.make}")
print('---------------------------')