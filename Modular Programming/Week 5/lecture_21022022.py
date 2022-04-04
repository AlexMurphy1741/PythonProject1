#iterate through a loop 1
# x = [6, 4, 2, 9, 7]
# length = len(x)
# for index in range(length):
#     x[index] *= 11
#     print(x[index])
# i=0  # alternative loops
# while i < length:
#     x[i] *= 10
#     i += 1

#iterate through loop method 2
# x = [6, 4, 2, 9, 7] # unlike first two loops will not change list will simply change copy of item in list
# for item in x:
#     print(item)

#mathod 3 enumerate
x = [6, 4, 2, 9, 7]
# for index, item in enumerate(x):
#     print(item)
#     x[index] *= 11
#
# y = 0 * 3
# y = [0] * 26
# z = x + y

# slicing returns a new list
# a = x[1:4:1] # first number specifies what index the number starts at last number states skips will go up like range
# b = x[0:4:2]
# x = [:4]
# d = [2:]
# e = [:]
# f = x[::-1]

if 5 in x:
    print("5 is in x")
#not in

x.append(4)
x = [5, 2, 7, 3, 9]
print(x)
y = [5, 2, 7, 3, 9]
y.insert(2, 4)
z = [5, 2, 7, 3, 9, 7, 7]
z.remove(7) # removes 7 from list
y = [5, 2, 7, 3, 9]
a = x.pop(3) # removes value at index 2 from x, also returns value: a become number 7
x.reverse() #reverse list order
x.sort() # sorts in increasing order
x.reverse()# no reverse sort so need to use sort and then reverse
a = x.count(3) # finds number of threes in the list is case-sensitive
b = x.index(7) # will crash if no value use else exception
c = x.copy()
d = len() #functions that can be used in lists
e = max()
f = min()
g = sum()





