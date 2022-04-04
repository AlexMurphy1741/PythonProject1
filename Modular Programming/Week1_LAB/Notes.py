def draw_eyes():
    flat_eyebrows = input("Does the face have flat eyebrows (Y/N): ").capitalize()
    while flat_eyebrows != "Y" and flat_eyebrows != "N":
        flat_eyebrows = input("Does the face have flat eyebrows (Y/N): ").capitalize()
    else:
        if flat_eyebrows == "Y":
            flat_eyebrows = True
            if flat_eyebrows == True:
                print("-  -")
                print("@  @")
        elif flat_eyebrows == "N":
            flat_eyebrows = False
            if flat_eyebrows == False:
                print("^  ^")
                print("@  @")


draw_eyes()