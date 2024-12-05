file = open("/home/eugene/PycharmProjects/advent2024/day2/input", 'r')
lines = file.read()
string = lines.splitlines()
# print(string[1][1])

safe = 0
input = []

for i in range(len(string)):
    input = string[i].split()
    int_input = []
    for element in input:
        int_input.append(int(element))

    print(type(int_input))