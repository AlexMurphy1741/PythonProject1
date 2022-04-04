def name_time(runners):
    name_of_runners = []
    time_of_runners = []
    for i in range(runners):
        while True:
            try:
                name = input("What is the runner's name: ")
                time = float(input("What is the runner's time: "))
                if len(name) > 1 and time > 0:
                    name_of_runners.append(name_of_runners)
                    time_of_runners.append(time_of_runners)
                    return name_of_runners, time_of_runners
                else:
                    print("Please provide a name with more than one character and a whole number greater than zero")
                    name = input("What is the runner's name: ")
                    time = float(input("What is the runner's time: "))
            except ValueError:
                print("Please provide a name with more than one character and a whole number greater than zero")
                name = input("What is the runner's name: ")
                time = float(input("What is the runner's time: "))
                if len(name) > 1 and time > 0:
                    name_of_runners.append(name)
                    time_of_runners.append(time)
                    return name_of_runners, time_of_runners