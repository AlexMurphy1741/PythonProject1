import math


def get_sides(side1: float, side2: float, side3: float,):
        a = side1
        b = side2
        c = side3
        return a, b, c

def calculate_s(side1:float, side2:float, side3:float,):
    a,b,c = get_sides(side1, side2, side3)
    num = a + b + c
    s = num / 2
    return s


def calculate_area(side1:float, side2:float, side3:float,):
    a,b,c = get_sides(side1, side2, side3)
    s = calculate_s(side1, side2, side3)
    sa = s - a
    sb = s - b
    sc = s - c
    sabc = sa * sb * sc
    sabc = s * sabc
    area = math.sqrt(sabc)
    return area


def main(side1:float, side2:float, side3:float,):
    get_sides(side1, side2, side3)
    calculate_s(side1, side2, side3)
    return calculate_area(side1, side2, side3)


# print(main(5.2, 4.0, 3.1))


#challenge 2


def ask_for_score():
    team1 = input("What is the name of the first team? ")
    team2 = input("What is the name of the second team? ")
    return team1, team2

def score_team1():
    d = 0
    team1, team2 = ask_for_score()
    while d < 1:
        d = d + 1
        tries = int(input(f"How many tries did {team1} score?"))
        tries = tries * 5
        conversion = int(input(f"How many conversions did {team1} score?"))
        conversions = conversion * 2
        drop_kick = int(input(f"How many drop kicks did {team1} score?"))
        drop_kick = drop_kick * 3
        penalty = int(input(f"How many penalties did {team1} score?"))
        penalty = penalty * 3
        score1 = tries + conversions + drop_kick + penalty
    else:
        tries = int(input(f"How many tries did {team2} score?"))
        tries = tries * 5
        conversion = int(input(f"How many conversions did {team2} score?"))
        conversions = conversion * 2
        drop_kick = int(input(f"How many drop kicks did {team2} score?"))
        drop_kick = drop_kick * 3
        penalty = int(input(f"How many penalties did {team2} score?"))
        penalty = penalty * 3
        score2 = tries + conversions + drop_kick + penalty
    return team1, score1, team2, score2





def determine_winner(score1, score2, team1, team2):
    if score1 > score2:
        return f"{team1} wins"
    elif score1 < score2:
        return f"{team2} wins"
    elif score1 == score2:
        return f"{team1} and {team2} drew"


def main():
    team1, score1, team2, score2 = score_team1()
    return determine_winner(score1, score2, team1, team2)


print(main())

