def print_banner():
    print("=" * 15)
    print("= Park Ticket =")
    print("=" * 15)


# print_banner()


def return_num_days(name:str, days:int):
    d = name
    x = days
    return d, x


# print(return_num_days("James", 8))

def return_cost_visiting_park(days:int):
    if days > 0 and days < 3:
        total_cost = days * 12.75
        print(f"The cost of visiting the park for {days} days is 12.75 per day costing {total_cost}")
    elif days > 2 and days < 6:
        total_cost = days * 10.75
        print(f"The cost of visiting the park for {days} days is 10.75 per day costing {total_cost}")
    elif days > 6:
        total_cost = days * 09.50
        print(f"The cost of visiting the park for {days} days is 9.50 per day costing {total_cost}")


return_cost_visiting_park(5)
return_cost_visiting_park(2)
return_cost_visiting_park(7)



print_banner()
name, days = return_num_days()
cost = return_cost_visiting_park()
