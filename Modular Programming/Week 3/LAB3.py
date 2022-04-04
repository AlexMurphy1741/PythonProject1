import math

import validation_functions


# Q1


def get_sides():
    """Two sides of triangle need to be provided as values"""
    num1 = validation_functions.read_positive_float("Enter the first number: ")
    num2 = validation_functions.read_positive_float("Enter the second number: ")
    return num1, num2


def determine_hypotenuse(num1, num2):
    num1 = num1 ** 2
    num2 = num2 ** 2
    num3 = num1 + num2
    hypotenuse = math.sqrt(num3)
    return hypotenuse


def main():
    num1, num2 = get_sides()
    hypotenuse = determine_hypotenuse(num1, num2)
    return hypotenuse


# print(main())
# Q2
def get_sides_triangle(num1: float, num2: float, num3: float):
    num1, num2, num3 = validation_functions.read_positive_float2(num1, num2, num3)
    return num1, num2, num3


def confirm_triangle_type(num1: float, num2: float, num3: float):
    num1, num2, num3 = get_sides_triangle(num1, num2, num3)
    if num1 == num2 and num2 == num3 and num1 == num3:
        return "Equilateral"
    elif num1 != num2 and num2 == num3 or num1 != num2 and num1 == num3 or num1 != num3 and num1 == num2 or num1 != num3 and num2 == num3:
        return "Isosceles"
    if num1 != num2 and num2 != num3 and num1 != num3:
        return "Scalene"


def displaying_triangle_type(num1: float, num2: float, num3: float, type: str):
    """Requires num1,2,3 and type of triangle"""
    return f"The lengths of the three sides are {num1}, {num2}, {num3}, and the type of triangle is {type}."


def main2(num1: float, num2: float, num3: float):
    num1, num2, num3 = get_sides_triangle(num1, num2, num3)
    typet = confirm_triangle_type(num1, num2, num3)
    return displaying_triangle_type(num1, num2, num3, typet)


# Q3.


def student_name():
    name = input("What is your name? ")
    surname = input("What is your surname? ")
    name = validation_functions.read_letters_and_spaces_only2(name)
    surname = validation_functions.read_letters_space_commas(surname)
    return name, surname


def students_grades(maths: int, irish: int, english: int):
    maths = validation_functions.read_positive_integer2(maths)
    irish = validation_functions.read_positive_integer2(irish)
    english = validation_functions.read_positive_integer2(english)
    return maths, irish, english


def calculate_average_grade(grade1: int, grade2: int, grade3: int):
    sum_grade = grade1 + grade2 + grade3
    average = sum_grade / 3
    return average


def exam_marks(grade1: int, grade2: int, grade3: int):
    average = calculate_average_grade(grade1, grade2, grade3)
    if average >= 70 and average <= 100:
        return "Excellent"
    elif average >= 40 and average < 70:
        return "Acceptable"
    elif average < 40:
        return "Failing"


def main(grade1: int, grade2: int, grade3: int):
    name1, name2 = student_name()
    print(name1, name2)
    grade1, grade2, grade3 = students_grades(grade1, grade2, grade3)
    print(grade1, grade2, grade3)
    average_grade = calculate_average_grade(grade1, grade2, grade3)
    average_grade = f"{average_grade:,.2f}"
    print(average_grade)
    return exam_marks(grade1, grade2, grade3)


print(main(25,55,75))

