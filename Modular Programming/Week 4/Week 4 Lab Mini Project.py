def driver_name():
    name1 = input("What is your name? ")
    while len(name1) < 1:
        name1 = input("What is your name? ")
    else:
        return name1


def date():
    date = "14 of February 2022"
    return date


def num_passengers():
    while True:
        try:
            passengers = int(input("How many passengers are in the car? "))
            if passengers > -1:
                return passengers
        except ValueError:
            pass


def price():
    passengers = num_passengers()
    d = 10
    c = 2.50 * passengers
    cost = c + d
    return passengers, cost


def print_ticket():
    ticket = input("Would you like a ticket to be printed(y/n)? ").upper()
    while ticket != "Y" and ticket != "N":
        ticket = input("Would you like a ticket to be printed(y/n)? ").upper()
    else:
        return ticket.upper()


def use_program(num=0):
    while num < 1:
        num += 1
        use = input("Do you wish to use my program (y/n)? ").capitalize()
        return num
    else:
        num -= 1
        use = input("Do you wish to use my program again (y/n)? ").capitalize()
        return num



def collate(num=0):
    use_program(num)
    name_driver = driver_name()
    today_date = date()
    number_of_pass, total_cost = price()
    ticket = print_ticket()
    statement = (
        f"====================\nDate:{today_date}\nName: {name_driver}\nNumber of passengers: {number_of_pass}\nTotal Cost: €{total_cost:,.2f}\n====================\n")
    return ticket, statement

def file_print(ticket, statement):
    if ticket == "Y":
        connection = open("file2.txt", "w")
        print(statement, file=connection)
        connection.close()
    else:
        print("Not")


def main(num=0):
    number = 0
    while number < 1:
        num += 1
        ticket, statement = collate(num)
        print(statement)
        file_print(ticket, statement)


main()
