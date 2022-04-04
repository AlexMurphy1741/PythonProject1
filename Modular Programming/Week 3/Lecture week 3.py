
# def convert_km_to_m(distance: float, distance2: float) -> float [float, float]:
#     """A tuple adds ect"""
#     distance = distance * 1000
#     distance2 = distance2 * 10000
#     return distance, distance2
#
#
# distance1, distance2 = convert_km_to_m(0.05, 0.003)
# print(distance1)
# print(distance2)


def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                break
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return number


# books = read_positive_integer("How many books? ")
# people = read_positive_integer("How many people? ")


def read_positive_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number >= 0:
                break
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_percent_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0 and number <= 100:
                break
            else:
                print("Provide a whole number between 0 and 100...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_percent_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number >= 0 and number <= 100:
                break
            else:
                print("Number between zero and one hundred please please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_letters_and_spaces_only(prompt):
    while True:
        users_input = input(prompt)
        if users_input.replace(" ", "").isalpha():
            break
        else:
            print("No non-alphabetic numbers allowed except for spaces")
    return users_input

# print(read_letters_and_spaces_only("_"))


