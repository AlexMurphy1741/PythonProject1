numbers = [4, 2, 7, 8]
# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))
# print(sum(numbers))
# for i in range(len(numbers)):
#     print(i, numbers[i])
# for i, item in enumerate(numbers):
#     print(i, item)
# c = numbers.copy()
# # print(c)
# print(f"{'numbers':10} {'copy':10}\n{'=' * 15}")
# for i, item in enumerate(numbers):
#     item += 1
#     num = 0
#     num += 1
#     print(f" {item:<10} {c[i]:<10}")

# Part 2
# import random
# number = int(input("Please provide a positive integer: "))
# x = 0
# numbers2 = []
# for x in range(0, number, 1):
#     j = random.randint(1,10)
#     numbers2.append(j)
# print(numbers2)
#
# numbers2.append(0)
# numbers2.append(0)
# print(numbers2)
#
#
# for i, item in enumerate(numbers2):
#      print(i, item)
#
#
# numbers2.reverse()
# print(numbers2)
#
#
# b = numbers2.index(4)
# while True:
#     try:
#         print(b)
#         break
#     except ValueError:
#         print("There is no 4 in the list") #Broken needs to be fixed
#     else:
#         print("There is no 4 in the list") #Broken needs to be fixed
#
#
# if 9 in numbers2:
#     print("The number 9 is in the list")
# else:
#     print("The number 9 is not contained in the list")
#
# c = random.randint(51,100)
# d = random.randint(51,100)
# print(c)
# print(d)
# numbers2.append(c)
# print(numbers2)
#
#
# numbers2.insert(3, d)
# print(numbers2)
#
# print(numbers2.count(50))
#
# over_fifty = 0
# over_fifty_list = []
# for item in numbers2:
#     while item > 50:
#         over_fifty += 1
#         over_fifty_list.append(item)
#         break
#     else:
#         pass
# print(over_fifty)
# print(over_fifty_list)
#
#
# a = numbers2.pop(1)
# print(numbers2)
#
# b = numbers2.count(5)
# count = 0
# while count < b:
#     count += 1
#     numbers2.remove(5)
#
# print(numbers2)
#
#
# while 7 in numbers2:
#     numbers2.remove(7)
#
# print(numbers2)

Part 3














