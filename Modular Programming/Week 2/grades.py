def level7_grade(number:int):
    if number > 0 and number < 40:
        return "Fail"
    elif number > 39 and number < 50:
        return "Pass"
    elif number > 49 and number < 60:
        return "Merit, Grade 2"
    elif number > 59 and number < 70:
        return "Merit, Grade1"
    elif number > 69 and number < 100:
        return "Distinction"

def level8_grade(number:int):
    if number > 0 and number < 40:
        return "Fail"
    elif number > 39 and number < 50:
        return "Pass"
    elif number > 49 and number < 60:
        return "Second Class Honours, Grade 2"
    elif number > 59 and number < 70:
        return "Second Class Honours, Grade 1"
    elif number > 69 and number < 100:
        return "First Class Honours"


def level9_grade(number:int):
    if number > 0 and number < 40:
        return "Fail"
    elif number > 39 and number < 60:
        return "Pass"
    elif number > 59 and number < 70:
        return "Merit"
    elif number > 69 and number < 100:
        return "Distinction"




