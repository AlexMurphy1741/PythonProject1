#Demonstrating reading from a file not in exam
def get_list_of_integers(filename):
    x = []
    with open(filename) as data:
        for line in data:
            x.append(int(line()))
    return x

def get_list_of_strings(filename):
    x = []
    with open(filename) as data:
        for line in data:
            x.append(line.strip())
    return x

def main():
    animals = get_list_of_strings("animal.txt")
    print(animals)
    ages = get_list_of_integers("animalages.txt")

if __name__ == '__main__':
    main()