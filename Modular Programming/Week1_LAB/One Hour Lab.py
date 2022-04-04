def draw_hair(number=1):
    number = number - 1
    print(" ######\n" * number, "######")


def draw_eyes(flat_eyebrows):
        if flat_eyebrows == True:
            print(" -  -")
            print(" @  @")
        if flat_eyebrows == False:
            print(" ^  ^")
            print(" @  @")


def draw_nose(character="u"):
    while len(character) < 0 or len(character) > 1:
        character = input(" Please enter a single character: ")
    else:
        print(f"  {character} ")


def draw_mouth():
    print(" ===")


def draw_face():
    flat_eyebrows = input("Does the face have flat eyebrows (Y/N): ").capitalize()
    while flat_eyebrows != "Y" and flat_eyebrows != "N":
        flat_eyebrows = input("Does the face have flat eyebrows (Y/N): ").capitalize()
    else:
        if flat_eyebrows == "Y":
            flat_eyebrows = True
        elif flat_eyebrows == "N":
            flat_eyebrows = False
    draw_hair(2)
    draw_eyes(flat_eyebrows)
    draw_nose("U")
    draw_mouth()


def main():
    draw_face()


main()
