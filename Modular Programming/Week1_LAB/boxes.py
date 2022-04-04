# Excercise 2


def main():
    print("Hello")


main()


def draw_tall_box(height:int):
    print("+", "-" * 5, "+")
    for k in range(height):
        print(" -     -")
    print("+", "-" * 5, "+")

def main():
    draw_tall_box(2)
    draw_tall_box(4)
    draw_tall_box(6)


main()

# Q2.


# def print_name_as_block(name:str):
#     print(f"{name}")
#     print(f"{len(name)}")
#     print(f"{name}")
#     print(f"{len(name)}")
#     print(f"{name}")
#     print(f"{len(name)}")
#     print(f"{name}")
#     print(f"{len(name)}")


def print_name_as_block(name:str):
    if len(name) > 6:
        print("")
    else:
        print(f"=" * len(name) * 4)
        for k in range(4):
            print(f"{name.upper()}" * 4)
        print(f"=" * len(name) * 4)


def main(name: str):
    print_name_as_block(name)


main("Dave")
main("James")
main("JamesMurphy")




# Q.3


def countdown(start_number = 10):
    start_number = int(input("Please provide a starting number: "))
    while start_number < 0 or start_number > 100:
        start_number = int(input("Please provide a starting number: "))
    else:
        for number in range(start_number,0,-1):
            print(f"{number}", end=' ')
        print("Blast Off!")


# Q.4

def show_tables(table_number):
    number = table_number
    if number < 1 or number > 12:
        print("error please enter a number between one and twelve inclusive")
    else:
        for i in range(1, 13):
            product = i * number
            print(f"{number} * {i} = {product}")


def main(table_number):
    show_tables(6)


main(6)




countdown()


