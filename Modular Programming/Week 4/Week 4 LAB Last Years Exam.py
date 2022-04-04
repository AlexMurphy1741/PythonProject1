def boxing_banner():
    print("=" * 18)
    print("= Boxing Weights =")
    print("=" * 18)


def boxers_weight():
    while True:
        try:
            weight = int(input("What is the boxer's weight: "))
            if weight >= 48:
                return weight
        except ValueError:
            pass # putting back into the loop


def get_data():
    n = input("What is the boxer's name: ")
    w = boxers_weight()
    return n, w


def data():
    name, weight = get_data()#capturing data as variables
    print(name)
    print(weight)


# main()


def confirm_weightclass(weight: int):
    if weight > 47 and weight < 51:
        return "Flyweight"
    elif weight > 51 and weight < 61:
        return "Lightweight"
    elif weight > 61:
        return "Heavyweight"
    else:
        return "Please provide a valid weight"


# print(confirm_weightclass(50))
# print(confirm_weightclass(55))
# print(confirm_weightclass(65))


def boxers_name_weight_category(name:str, weight: int, category: str):
    print(f"{name} ({weight}kg) is a {category}")


# boxers_name_weight_category("Brian", 53, "Lightweight")


def main():
    name, weight = get_data()
    category = confirm_weightclass(weight)
    boxing_banner()
    boxers_name_weight_category(name, weight, category)


main()


