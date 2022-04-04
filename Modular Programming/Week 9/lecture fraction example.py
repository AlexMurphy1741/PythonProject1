class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def decimal(self):
        return self.numerator / self.denominator


def main():
    x = Fraction(3, 4)
    print(x)
    y = Fraction(4, 5)
    print(y, y.decimal)


def ____main__():
    dog1 = Dog("Esme", 7, "Lurcher")
    dog2 = Dog("Ruby", 5, "Mongrel")
    print(dog1)

    def convert_to_dog_years(self):
        CONVERSION = 7
        return self.age * CONVERSION


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old"
