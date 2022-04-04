# Part 1

def find_larger_number(num1:int,num2:int):
    number = 0
    if num1 > num2:
        number = num1
    elif num2 > num1:
        number = num2
    elif num2 == num1:
        number = num1
    return number


def find_larger_string(word1:str, word2:str):
    if word1 > word2:
        string = word1
    elif word2 > word1:
        string = word2
    elif word2 == word1:
        string = word2
    return string


def surname_firstname(name1:str, name2:str):
    return f"{name2},{name1}"


def fizz_buzz_game(number:int):
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    else:
        return number


def percentage_of_landmass(country:str, area:int):
    world_landmass = 148940000
    percent_area = area / world_landmass
    percent_area = percent_area * 100
    return f"{country} is {percent_area:,.2f}% of the total world's landmass"


def add_numbers(num1:str, num2:str):
    number1 = int(num1)
    number2 = int(num2)
    number3 = number1 + number2
    number3 = str(number3)
    return number3


def radius_of_circle(radius: int):
    import math
    radius = radius * radius
    number = math.pi * radius
    print(f"A circle of radius {radius} has an area of {number:,.2f}")







