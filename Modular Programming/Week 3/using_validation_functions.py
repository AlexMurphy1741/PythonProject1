import validation_functions

#
# def display_personal_details(n, a, g):
#     print(f"Name: {n}")
#     print(f"Age: {a}")
#     print(f"grade: {g:.0f}%")
#
#
# if __name__ == '__main__':
#     name = validation_functions.read_letters_and_spaces_only("Name? ")
#     age = validation_functions.read_positive_integer(f"What age is {name}? ")
#     grade = validation_functions.read_percent_float(f"What grade did {name} receive? ")
#     display_personal_details(name, age, grade)

# print(display_personal_details())


def write_minutes_title_of_movie():
    return minutes, title


if __name__ == '__main__':
    title = validation_functions.read_letters_and_spaces_only("What is the title of the movie? ")
    minutes = validation_functions.read_positive_integer("How long is the movie? ")
    write_minutes_title_of_movie()


length, Name = write_minutes_title_of_movie()
print(length)
print(Name)
