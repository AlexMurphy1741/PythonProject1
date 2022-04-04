# # Q1 a
# numbers = [4, 2, 7, 8]
#
# #b
#
# print(numbers[0])
#
# #c
# print(numbers[-1])
#
# #d
#
# print(len(numbers))
#
# #e
# print(sum(numbers))
#
# #f
# for i in range(len(numbers)):
#     number = numbers[i]
#     print(i, number)
#
#
#
# #g
#
# for i, item in enumerate(numbers):
#     print(i, item)
# # h
# numbers2 = numbers.copy()
# print(numbers2)
#
# #i
# print(numbers)
# for i in range(len(numbers)):
#     numbers[i] += 1
# print(numbers)
#
#
# #j
# print(f"{'numbers':10}{'copy':10}\n{'=' * 15}")
# for i in range(len(numbers)):
#     print(f"{numbers[i]:<10} {numbers2[i]:<10}")
# Part 2
#a
# import random
# number = int(input("Please provide a positive integer: "))
# numbers2 = []
# for i in range(0, number, 1):
#     j = random.randint(1, 10)
#     numbers2.append(j)
# print(numbers2)
#
# #b
#
# numbers2.pop(-1)
# numbers2.pop(-2)
# numbers2.append(0)
# numbers2.append(0)
# print(numbers2)
#
# #c
#
# for i, item in enumerate(numbers2):
#     print(i, item)
#
# #d
# numbers2.reverse()
# print(numbers2)
#
#
# #e
# x = 0
# while True:
#     try:
#         x = numbers2.index(4)
#         print(x)
#         break
#     except ValueError:
#         print("That value is not contained in the list, please try another")
#         break
#     else:
#         print("That value is not contained in the list, please try another")
#         break
# #f
#
# if 9 in numbers2:
#     print(f"Nine is present on the list at index {numbers2.index(9)}")
# else:
#     print("Nine is not a number in the list, please try another")
#
# #g
# y = random.randint(1, 10)
# numbers2.append(y)
#
# #h
# z = random.randint(1, 10)
# numbers2.insert(3, z)
# print(numbers2)
#
# #i
#
# count_5 = numbers2.count(5)
# print(count_5)
#
# #j
# numbers3 = []
# x = 0
# for i, item in enumerate(numbers2):
#     if item >= 5:
#         x += 1
#         numbers3.append(item)
# print(x, numbers3)
#
# #k
#
# numbers2.pop(1)
# print(numbers2)
#
# #l
# numbers2.append(5)
# numbers2.append(5)
# numbers2.append(5)
# numbers2.append(5)
# numbers2.append(5)
# numbers2.append(5)
# numbers2.append(5)
# print(numbers2)
#
# num = 0
# for i, items in enumerate(numbers2):
#     if items == 5:
#         num += 1
#     else:
#         pass
#
# for i in range(0, num, 1):
#     numbers2.remove(5)
# print(numbers2)
#
# # j
#
# while 7 in numbers2:
#     try:
#         numbers2.remove(7)
#     except ValueError:
#         pass
# else:
#     pass
#
# print(numbers2)

#part3

#a
# countries = ["spain", "brazil", "portugal", "bolivia"]
#
# #b
#
# for i, item in enumerate(countries):
#     print(item)
#
#
# #c
# country = []
# for i in range(len(countries)):
#     country.append(countries[i].capitalize())
# countries = country
# print(countries)
#
# #d
#
# countries.append("Italy")
# print(countries)
#
# #e
#
# countries.pop(-2)
# print(countries)
#
# countries.append("Bolivia")
# print(countries)
# countries.remove("Bolivia")
# print(countries)
#
# #f
#
#
# country = input("Provide a country ")
# countries.append(f"{country}")
# print(countries)
#
# #g
# group1 = countries[0:3:1]
# group2 = countries[3:5:1]
# print(group1)
# print(group2)
#
# #h
# for i in range(len(group1)):
#     print(group1[i])
# print("---------------------")
# for i in range(len(group2)):
#     print(group2[i])


#Q4
# #a
# import random
# random_numbers = []
# for i in range(1, 31, 1):
#     random_number = random.randint(1, 10)
#     random_numbers.append(random_number)
# print(random_numbers)
# #b
# even_number = 0
# odd_number = 0
# number_of_tens = 0
# number_of_ones = 0
# even_list = []
# not3_list = []
# for i in range(len(random_numbers)):
#     if random_numbers[i] % 2 == 0:
#         even_number += 1
#         even_list.append(random_numbers[i])
#     if random_numbers[i] % 3 == 0:
#         odd_number += 1
#     if random_numbers[i] == 10:
#         number_of_tens += 1
#     if random_numbers[i] == 1:
#         number_of_ones += 1
#     if random_numbers[i] % 3 != 0:
#         not3_list.append(random_numbers[i])
# print(number_of_tens)
# print(even_number)
# print(odd_number)
# print(number_of_ones)
# print(even_list)
# print(not3_list)
# Q5
#
#
# scores = [9, 8, 6, 7, 6]
# judges = ["Kim", "Tim", "Finn", "Lynn", "Wynn"]
# total = sum(scores)
# print(total)
# average = total / len(scores)
# print(average)
# total2 = 0
# for i in range(len(scores)):
#     total2 += scores[i]
# print(total2)
# average2 = total2 / len(scores)
# print(average2)
#
# #b
#
# minimum = min(scores)
# maximum = max(scores)
# print(minimum, maximum)
#
# #c
#
# # for i in range(len(scores)):
# #     min_score = min(scores)
# #     index, index2 = scores.index(min_score)
# #     judge1, judge2 = judges.index(index, index2)
# # print(judge1)
# # print(judge2)
# # not working
# #d
# scores_greater_7 = 0
# for i in range(len(scores)):
#     if scores[i] > 7:
#         scores_greater_7 += 1
#     else:
#         pass
# print(scores_greater_7)
#
# #e
# min_score = min(scores)
# total_score = sum(scores)
# scores_not_min = total_score - min_score
#
# if scores_not_min > 32:
#     print("You have made it through to the next round.")
# elif scores_not_min < 32:
#     print("You have not made it through to the next round")
#
#
# #f
# judges = ["Kim", "Tim", "Finn", "Lynn", "Wynn"]
# judge_name = input("Provide a name of a judge: ")
# judge_name = f'{judge_name}'
# if judge_name in judges:
#     try:
#         index_name = judges.index(judge_name)
#         judges.remove(judge_name)
#         scores.pop(index_name)
#     except ValueError:
#         pass
# else:
#     judge_name = input("Provide a name of a judge: ")
# print(judges)
# print(scores)

#Q6
#a
# runner = []
# time = []
# for i in range(1, 5, 1):
#     runner.append(input("Please provide a name: "))
#     time.append(int(input("Please provide their time: ")))
# min_time = min(time)
# winner_index = time.index(min_time)
# winner = runner[winner_index]
# print(f"{winner}, {min_time}")

#d
# runner = []
# time = []
# winners_time = []
# winners = []
# draw = []
# for i in range(1, 5, 1):
#     runner.append(input("Please provide a name: "))
#     time.append(int(input("Please provide their time: ")))
#     min_time = min(time)
#     winner_index = time.index(min_time)
#     winner = runner[winner_index]
# for j in range(len(time)):
#     if time[j] == min_time:
#         winners_time.append(time[j])
#         winners.append(runner[j])
#     else:
#         pass
# if len(winners) > 0 and len(winners) < 2:
#     print(f"The race was won by {winners[0]}")
# elif len(winners) > 1 and len(winners) < 3:
#     for g in range(len(winners)):
#         draw.append(winners[g])
#     a, b = winners
#     print(f"The race was a draw between {a} and {b}")
# elif len(winners) > 2 and len(winners) < 4:
#     for h in range(len(winners)):
#         draw.append(winners[h])
#     a, b, c = winners
#     print(f"The race was a draw between {a}, {b} and {c}")
# elif len(winners) > 3:
#     for k in range(len(winners)):
#         draw.append(winners[k])
#     a, b, c, d = winners
#     print(f"The race was a draw between {a}, {b}, {c} and {d}")

#e
#
# runner = []
# time = []
# winners_time = []
# winners = []
# runners_up = []
# runners_up_time = []
# draw = []
# for i in range(1, 5, 1):
#     runner.append(input("Please provide a name: "))
#     time.append(int(input("Please provide their time: ")))
#     min_time = min(time)
#     winner_index = time.index(min_time)
#     winner = runner[winner_index]
# for j in range(len(time)):
#     if time[j] == min_time:
#         winners_time.append(time[j])
#         winners.append(runner[j])
#     elif time[j] != min_time:
#         runners_up_time.append(time[j])
#         runners_up.append(runner[j])
#     else:
#         pass
# if len(winners) > 0 and len(winners) < 2:
#     print(f"The race was won by {winners[0]}")
#     print(f"{runners_up[0]} was {runners_up_time[0] - winners_time[0]} seconds behind.")
#     print(f"{runners_up[1]} was {runners_up_time[1] - winners_time[0]} seconds behind.")
#     print(f"{runners_up[2]} was {runners_up_time[2] - winners_time[0]} seconds behind.")
# elif len(winners) > 1 and len(winners) < 3:
#     for g in range(len(winners)):
#         draw.append(winners[g])
#     a, b = winners
#     print(f"The race was a draw between {a} and {b}")
#     print(f"{runners_up[0]} was {runners_up_time[0] - winners_time[0]} seconds behind.")
#     print(f"{runners_up[1]} was {runners_up_time[1] - winners_time[0]} seconds behind.")
#
# elif len(winners) > 2 and len(winners) < 4:
#     for h in range(len(winners)):
#         draw.append(winners[h])
#     a, b, c = winners
#     print(f"The race was a draw between {a}, {b} and {c}")
#     print(f"{runners_up[0]} was {runners_up_time[0] - winners_time[0]} seconds behind.")
#
# elif len(winners) > 3:
#     for k in range(len(winners)):
#         draw.append(winners[k])
#     a, b, c, d = winners
#     print(f"The race was a draw between {a}, {b}, {c} and {d}")

# Q. Challenge1

# amountOfRain = [117.1, 52.34, 88.8, 16.0, 137.3, 54.3]
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# for k in range(len(amountOfRain)):
#     a = amountOfRain[k] // 10
#     a = int(a)
#     stars = "*" * a
#     print(months[k])
#     print(stars)
#     min_rain = min(amountOfRain)
#     max_rain = max(amountOfRain)
#     index_max = amountOfRain.index(max_rain)
#     index_min = amountOfRain.index(min_rain)
#     print(f" {months[index_max]} is the wettest month")
#     print(f" {months[index_min]} is the driest month")
# Q. Challenge2
#
#
# numbers = []
# import random
#
#
# def user_number():
#     try:
#         if True:
#             number = int(input("Enter a positive whole number: "))
#             number += 1
#             return number
#     except ValueError:
#         print("Error, please enter a positive whole number.")
#         number = int(input("Enter a positive whole number: "))
#         number += 1
#     return number
#
#
# def random_list(number):
#     for i in range(1, number):
#         random_number = (random.randint(1, 11))
#         numbers.append(random_number)
#     return numbers
#
#
# def table_random():
#     number = user_number()
#     number = number
#     number2 = number - 1
#     numbers = random_list(number)
#     print(number)
#     print(numbers)
#     print(f"{'Number':<10} {'Occurrences':<10}")
#     print("=" * 22)
#     for i in range(0, number2):
#         x = numbers.count(numbers[i])
#         j = i + 1
#         print(f"{numbers[i]:^10} {x:^10}")
#
#
# table_random()
#Q9.


numbers = []
import random


def user_number():
    try:
        if True:
            number = int(input("Enter a positive whole number: "))
            number += 1
            return number
    except ValueError:
        print("Error, please enter a positive whole number.")
        number = int(input("Enter a positive whole number: "))
        number += 1
    return number


def random_list(number):
    for i in range(1, number):
        random_number = (random.randint(1, 11))
        numbers.append(random_number)
    return numbers


def table_random():
    number = user_number()
    number = number
    number2 = number - 1
    numbers = random_list(number)
    most_common_number = 1
    most_occurrences = 1
    print(number)
    print(numbers)
    print(f"{'Number':<10} {'Occurrences':<10}")
    print("=" * 22)
    xs = []
    for i in range(0, number2):
        x = numbers.count(numbers[i])
        xs.append(x)
        j = i + 1
        print(f"{numbers[i]:^10} {x:^10}")
        print("")
        if x > most_common_number:
            most_common_number = numbers[i]
            most_occurrences = x
        else:
            pass
    if most_occurrences > 1:
        print(f"The most common number is {most_common_number}")
    else:
        print("No number occurs more than once.")


table_random()


























