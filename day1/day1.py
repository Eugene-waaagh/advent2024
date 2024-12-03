file = open("/home/eugene/PycharmProjects/advent2024/day1/input", 'r')
lines = file.read()
string = lines.split()

input = []

for num in string:
    input.append(int(num))

right = []
left = []

for i, num in enumerate(input):
    if i % 2 == 0:
        right.append(num)
    else:
        left.append(num)

sorted_left = sorted(left)
sorted_right = sorted(right)

total = 0
for num_left, num_right in zip(sorted_left, sorted_right):
    if num_left >= num_right:
        total = total + (num_left - num_right)
    else:
        total = total + (num_right - num_left)

print(total)


