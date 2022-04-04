from grades import *

def your_grade():
    grade = int(input("Please provide a grade between 0 and 100: "))
    return grade

def your_course_level():
    degree = int(input("What is the level of your degree (7, 8, 9): "))
    return degree


def main():
    grade = your_grade()
    degree = your_course_level()
    if degree == 7:
        grade = level7_grade(grade)
        return f"Your grade is: {grade}"
    elif degree == 8:
        grade = level8_grade(grade)
        return f"Your grade is: {grade}"
    elif degree == 9:
        grade = level9_grade(grade)
        return f"Your grade is: {grade}"


print(main())

# Data Comes from a file

