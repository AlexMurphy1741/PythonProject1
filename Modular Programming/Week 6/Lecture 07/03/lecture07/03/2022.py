def get_data(filename):
    strings = []
    integers = []
    floats = []
    with open(filename) as data:
        for line in data:
            line_list = line.strip().split(',')
            strings.append(line_list[0])
            integers.append(int(line_list[1]))
            floats.append(float(line_list[2]))
    return strings, integers, floats

def main():
    animals, ages, weight = get_data("animaldata.txt")
    print(animals, ages, weight)


if __name__ == '__main__':
    main()