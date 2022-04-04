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


# print(read_letters_and_spaces_only("What is the name:"))


def read_positive_float2(num1: float, ):
    while True:
        try:
            if num1 >= 0:
                break
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return num1


def read_positive_integer2(num1):
    while True:
        try:
            number = num1
            if number >= 0:
                break
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_percent_integer2(num1):
    while True:
        try:
            number = num1
            if number >= 0 and number <= 100:
                break
            else:
                print("Provide a whole number between 0 and 100...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_percent_float2(num1):
    while True:
        try:
            number = num1
            if number >= 0 and number <= 100:
                break
            else:
                print("Number between zero and one hundred please please...")
        except ValueError:
            print("Must be numeric...")
    return number


def read_letters_and_spaces_only2(word1):
    while True:
        users_input = word1
        if users_input.replace(" ", "").isalpha():
            break
        else:
            print("No non-alphabetic numbers allowed except for spaces")
            break
    return users_input


def read_letters_space_commas(word1):
    while True:
        users_input = word1
        users_input2 = users_input.replace("'", "")
        if users_input2.replace(" ", "").isalpha():
            break
        else:
            print("No non-alphabetic numbers allowed except for spaces")
            break
    return users_input
