def draw_box():
    print("+------+")
    for k in range(3):
        print("-      -")
    print("+------+")


def draw_nose():
    print("   / \\")
    print("  /   \\")
    print(" /     \\")
    print("/       \\")


def draw_thrusters():
    print("  // \\\\")
    print(" //   \\\\")
    print("//     \\\\")


def draw_shuttle():
    draw_nose()
    draw_box()
    draw_thrusters()


def main():
    draw_shuttle()


# main()


# Section 2



