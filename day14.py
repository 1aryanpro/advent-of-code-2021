input = open("inputs/day14input.txt").readlines()
poly = input[0][:-1]
rules = dict([line[:-1].split(" -> ") for line in input[2:-1]])


def insert(index, char):
    print((list(poly).insert(index, char)))
    return "".join(list(poly).insert(index, char))


def step():
    newpoly = poly + ""
    for i in range(len(newpoly)):
        pair = newpoly[i:i+2]
        if pair in rules:
            newpoly = insert(i, rules[pair])
    return newpoly


step()
print(poly)

