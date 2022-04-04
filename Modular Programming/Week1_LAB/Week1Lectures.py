# Task 1
def writeline():
    print("=" * 23)


def print_my_name():
    print("Alex")


def say_hello():
    writeline()
    print("Hello from my program")
    writeline()


def say_goodbye():
    writeline()
    print("Goodbye from my program")
    writeline()


def main():
    print_my_name()
    say_hello()
    say_goodbye()


main()


# Task 2

def draw_full_line():
    print("+", "=" * 10, "+")


def draw_gappy_line():
    print("-", " " * 10, "-")


def draw_a_box():
    draw_full_line()
    for k in range(3):
        draw_gappy_line()
    draw_full_line()


def main():
    for k in range(3):
        draw_a_box()


main()


def draw_nose():
    print("    /    \\")
    print("   /      \\")
    print("  /        \\")
    print(" /          \\")


def draw_plume():
    print("   //    \\\\")
    print("  //      \\\\")
    print(" //        \\\\")
    print("//          \\\\")


def draw_shuttle():
    draw_nose()
    for k in range(3):
        draw_a_box()
    draw_plume()


def main():
    draw_shuttle()


main()


def sing(name: str):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print(f"Happy birthday dear {name}")
    print("Happy birthday to you\n")


def main(name: str):
    (sing(name))


main("Sarah")
main("Ian")
main("Nicola")


def main2():
    name = input("What is your name: ")
    sing(name)


main2()


