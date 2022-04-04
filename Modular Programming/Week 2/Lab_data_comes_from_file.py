# def grades_from_file():
#     with open("newfile.txt", "r") as grade:
#         for line in grade:
#             grade = line
#             grade = grade.split()
#             grade1 = grade[0]
#             grade2 = grade[1]
#             print(grade1)
#
#
#
# grades_from_file()
#
#
# def unpacking_grades():
#     grade1, grade2, grade3, grade4 = grades_from_file()
#     print(grade1)
#
#
def unpacking_grades2():
    grade1 = 45
    grade2 = 56
    grade3 = 34
    grade4 = 89
    return grade1, grade2, grade3, grade4,
# Not finished
#
# def write_to_file():
#     grade1, grade2, grade3, grade4, = unpacking_grades
#     statement = f"{grade1},{grade2},{grade3},{grade4}"
#     file = input("What is the name of the file you wish to write to: ")
#     details = open(f"{file}", "w")
#     print(statement, file=details)
#     details.close


def write_to_file(file_name):
    grade1, grade2, grade3, grade4, = unpacking_grades2()
    a = input(file_name)
    statement = f"{grade1},{grade2},{grade3},{grade4}"
    details = open(f"{file_name}", "w")
    print(statement, file=details)
    details.close
    return statement



marks_file = write_to_file("What is the name of the input file?")
output_file = write_to_file("What is the name of the file to store the results?")

