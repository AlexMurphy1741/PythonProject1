connection = open("newfile.txt", "a")
print("Alex", file=connection)
connection.close()

with open("newfile.txt", "r") as reading:
    for line in reading:
        print(line)
connection.close()

