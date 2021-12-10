input = open('inputs/day2.txt', 'r').readlines()
arr = [y.split(" ") for y in input]

x = y = a = 0

for [cmd, s] in arr:
    s = int(s)
    if (cmd == 'forward'):
        x += s
        y += s * a
    elif (cmd == 'down'):
        a += s
    elif (cmd == 'up'):
        a -= s


print(f"{x = }")
print(f"{y = }")

print(f"{x*y = }")
