import math


def surface_area(radius: float, height: float):
    radius2 = radius * radius
    pi2 = 2 * math.pi
    two_pi_r = pi2 * radius2
    two_pi_r_h = pi2 * radius * height
    area = two_pi_r_h + two_pi_r
    return area


def distance_meters(dis: int):
    selection = int(input("Please select an option between one and four: "))
    if selection == 1:
        meters = dis / 1000
        return meters
    elif selection == 2:
        feet = dis / 3.248084
        return feet
    elif selection == 3:
        inches = dis / 39.3701
        return inches
    elif selection == 4:
        quit


def distance(x1:int, y1:int, x2:int, y2: int):
    x = x2 - x1
    x = x ** 2
    y = y2 - y1
    y = y ** 2
    xy = x + y
    d = math.sqrt(xy)
    return d


print(distance(5, 4, 3, 2))
