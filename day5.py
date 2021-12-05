input = open('inputs/day5.txt', 'r').read().split('\n')
lines = [l.replace(" -> ", " ").replace(",", " ").split() for l in input[:-1]]

size = 1000
matrix = [[0]*size for i in range(size)]

for i in range(len(lines)):
    lines[i] = [int(n) for n in lines[i]]

for line in lines:
    x1, y1, x2, y2 = line
    if x1 > x2:
        x2, x1 = x1, x2
        y2, y1 = y1, y2
    if x1 == x2:
        if y1 > y2: y2, y1 = y1, y2
        for i in range(y1, y2+1):
            matrix[i][x1] += 1
    elif y1 == y2:
        for i in range(x1, x2+1):
            matrix[y1][i] += 1
    else:
        slope = 1 if y2 > y1 else -1
        for i in range(x2 - x1 + 1):
            matrix[y1 + i * slope][x1 + i] += 1



count = 0
for row in matrix:
    for el in row:
        if el > 1: count += 1

print(count)
