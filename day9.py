input = open('inputs/day9.txt').readlines()
input = [f"9{line[:-1]}9" for line in input][:-1]
input = ["9" * (len(input[0]))] + input + ["9" * len(input[0])]
input = [list(map(int, line)) for line in input]

def lowPoint(y, x):
    if (curr := input[y][x]) > 8: return 0
    bot = input[y + 1][x]
    top = input[y - 1][x]
    lef = input[y][x - 1]
    rig = input[y][x + 1]
    dirs = [bot, top, lef, rig]

    return all(map(lambda n: curr < n, dirs))

def basin(y, x):
    input[y][x] = 10
    output = 1

    for i in [-1, 1]:
        if lowPoint(y, x+i): output += basin(y, x+i)
        if lowPoint(y+i, x): output += basin(y+i, x)

    return output

count = 0
basins = []
for y in range(1, len(input) - 1):
    for x in range(1, len(input[0]) - 1):
        if lowPoint(y, x):
            basins.append(basin(y, x))

basins = sorted(basins)
for l in input: print("".join(map(lambda c: str(c) if c != 10 else 'v',l)))
print(basins[-1] * basins[-2] * basins[-3])
