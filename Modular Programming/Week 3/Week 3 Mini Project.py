import validation_functions


def ask_for_name():
    team1 = input("What is the name of the first team? ")
    team2 = input("What is the name of the second team? ")
    return team1, team2

def score_team1():
    num = 0
    team1, team2 = ask_for_name()
    while num < 1:
        num += 1
        points = validation_functions.read_positive_integer(f"How many points did {team1} score?")
        points = points
        goals = validation_functions.read_positive_integer(f"How many goals did {team1}  score?")
        goals = goals * 3
        score1 = points + goals
    else:
        num += 1
        points = validation_functions.read_positive_integer(f"How many points did {team2} score?")
        points = points
        goals = validation_functions.read_positive_integer(f"How many goals did {team2} score?")
        goals = goals * 3
        score2 = points + goals
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

