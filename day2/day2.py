file = open("/home/eugene/PycharmProjects/advent2024/day2/input", 'r')
lines = file.read()
string = lines.splitlines()
# print(string[1][1])

# Part 1
safe = 0

for line in string:
    row = line.split()
    int_row = []
    for element in row:
        int_row.append(int(element))

    safe_check = True
    is_increasing = True
    is_decreasing = True

    for i in range (len(int_row) - 1):
        current = int_row[i]
        next = int_row[i +1]

        difference = abs(current - next)

        if difference > 3 or difference < 1:
            safe_check = False
            break

        if current < next:
            is_decreasing = False
        elif current > next:
            is_increasing = False
        elif current == next:
            safe_check = False
            break

    if safe_check and (is_increasing or is_decreasing):
            safe += 1

print("Part 1:",safe)
# End of Part 1#

# Part 2


