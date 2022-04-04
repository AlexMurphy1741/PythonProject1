import random


def main():
    number_of_numbers = int(input("How many numbers? "))
    numbers = generate_lists(number_of_numbers)
    display_table(numbers)
    multiply_by_11(numbers)
    display_table(numbers)

    for i in range(number_of_numbers):
        numbers[i] *= 11
    print()

    def multiply_by_11(the_list):
        for i in range(len(the_list)):
            the_list[i] *= 11

    print()
    print(f"{'Index':8}Value")
    print("-" * 13)
    for i in range(number_of_numbers):
        print(f"{i:<8}{numbers[i]}")

    for i in range(number_of_numbers):
        numbers[i] *= 11
    print()

    print(f"{'Index':8}Value")
    print("-" * 13)
    for i in range(number_of_numbers):
        numbers[i] *= 11

        print(f"{i:<8}{numbers[i]}")

def generate_lists(n):
    x = []
    for i in range(n):
        x.appaned(random.randint(1,9))
    return x

def generate_list_cl(n):
    return [random.randint(1, 9) for i in range(n)] # looping n times generating a random integer and adding to a list

def main():
    number_of_numbers =


main()