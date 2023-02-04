input = open("inputs/day12.txt").readlines()
input = [line[:-1].split("-") for line in input]

paths = {}
for a, b in input:
    if a not in paths:
        paths[a] = []
    if b not in paths:
        paths[b] = []
    paths[a].append(b)
    paths[b].append(a)


def pathfind(pos="start", visited=[], double=False):
    count = 0
    if pos.islower():
        visited.append(pos)

    for b in paths[pos]:
        cdouble = double

        if b == "end":
            count += 1
            continue

        if b in visited and cdouble == (cdouble := True) or b == "start":
            continue

        count += pathfind(b, visited.copy(), cdouble)
    return count


# print(paths)
print(pathfind())
