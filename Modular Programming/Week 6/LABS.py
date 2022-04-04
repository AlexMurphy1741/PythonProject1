#Labs Week 6
# def race_name():
#     name = input("What is the name of the race: ")
#     runners = int(input("How many runners participated in the race: "))
#     while True:
#         try:
#             if runners > 0 and len(name) > 1:
#                 return name, runners
#             else:
#                 print("Please provide a positive whole number")
#                 runners = int(input("How many runners participated in the race: "))
#         except ValueError:
#             print("Please provide a name of greater than one character and a positive whole number")
#             name = input("What is the name of the race: ")
#             runners = int(input("How many runners participated in the race: "))
#
# def name_time(runners):
#     name_of_runners = []
#     time_of_runners = []
#     for i in range(runners):
#         try:
#             name = input("What is the runner's name: ")
#             time = float(input("What is the runner's time: "))
#             name_of_runners.append(name)
#             time_of_runners.append(time)
#         except ValueError:
#                 print("Please provide a name with more than one character and a whole number greater than zero")
#                 name = input("What is the runner's name: ")
#                 time = float(input("What is the runner's time: "))
#     return name_of_runners, time_of_runners
#
#
# def average_times(time_of_runners):
#     average_time = sum(time_of_runners)
#     x = len(time_of_runners)
#     average_time = average_time / x
#     return average_time
#
#
# def over_25(name_of_runners, time_of_runners):
#     runners_over_25 = []
#     for k in range(len(name_of_runners)):
#         if time_of_runners[k] > 25.0:
#             runners_over_25.append(name_of_runners[k])
#         else:
#             pass
#     return runners_over_25
#
#
# def modified_times(time_of_runners):
#     modified_times_10 = []
#     for k in range(len(time_of_runners)):
#         modified_time = time_of_runners[k] * 0.90
#         modified_times_10.append(modified_time)
#     return modified_times_10
#
#
# def main():
#     print("111517317")
#     name, runners = race_name()
#     print(f"The name of the race is {name} which has {runners} participants.")
#     name_of_runners, time_of_runners = name_time(runners)
#     runners_over_25 = over_25(name_of_runners, time_of_runners)
#     modified_time = modified_times(time_of_runners)
#     for k in range(runners):
#         print(f"{name_of_runners[k]}'s time when ten percent faster is {modified_time[k]:,.2f}")
#     for g in range(len(runners_over_25)):
#         h = g + 1
#         print(f"{runners_over_25[g]} took over 25 minutes")
#     for k in range(len(name_of_runners)):
#         j = k + 1
#         print(f"Runner Number {j} is {name_of_runners[k]} who got a time of {time_of_runners[k]}")
#     print(f"The average time of the runners is {average_times(time_of_runners)}")
#
#
# main()
#Q1.
#
# string = "the cat in the hat"
#
# def word_count(word):
#     letters = 0
#     for character in string:
#         if character == "a":
#             letters += 1
#         print(letters)
#
#
# def vowels_count(word):
#     letters = 0
#     vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
#     for character in string:
#         if character in vowels:
#             letters += 1
#         print(letters)
#
#
# word1 = "Hello"
# word2 = "Hello"
#
#
# def length_comparison(word1, word2):
#     letters = 0
#     length1 = len(word1)
#     length2 = len(word2)
#     for character in string[0]:
#         if length1 == length2 and character[0]:
#             print("Word1 and Word2 are the same length and start with the same letter")
#         else:
#             print("The two words are not the same length or do not start with the same letter")
#
#
# # length_comparison(word1, word2)
# #Q2
#
# def get_numbers():
#     x = []
#     for i in range(10):
#         number = int(input("Number? "))
#     x.append(number)
#     return x
#
# #a
#
# def get_words():
#     words = []
#     for i in range(10):
#         word = input("Word? ")
#         words.append(word)
#     return words
#
#
# #b
#
# def words_same_letter(words, letter):
#     new_list = []
#     for i in range(len(words)):
#         word = words[i]
#         for char in word[0]:
#             if char == letter:
#                 word_a = word
#                 new_list.append(word_a)
#     return new_list
#
#
# #c
#
#
# def words_letter_b(words, letter):
#     a_list = []
#     words = words.split()
#     for i in range(len(words)):
#         word = words[i]
#         for char in word[0]:
#             if char == letter:
#                 word_a = word
#                 a_list.append(word_a)
#     return a_list
#
#
#
#
#
# def main():
#     word = get_words()
#     length = len(word)
#     letter1 = "a"
#     letter2 = "s"
#     string1 = "apple orange banana amazing aperture flower anemone"
#     print(words_same_letter(word, letter2))
#     print(words_letter_b(string1, letter1))
#     print("X" * 15)
#     for j in range(length):
#         print(word[j])
#
#
# main()
#Q3





