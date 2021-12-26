input = open('inputs/day12test3.txt').readlines()
input = [l[:-1].split('-') for l in input]

paths = {}
for a,b in input:
    if a not in paths: paths[a] = []
    if b not in paths: paths[b] = []
    paths[a].append(b)
    paths[b].append(a)

def pathfind(pos = 'start', visited = [], double = False, path = []):
    count = 0
    if pos.islower(): visited.append(pos)
    path.append(pos)

    for b in paths[pos]:
        if b == 'end':
            count += 1
            path.append(b)
            print(",".join(path))
            continue
        if b in visited:
            if double or b == 'start': continue
            double = True
        count += pathfind(b, visited.copy(), double, path.copy())
    return count

def pathfind2(pos = 'start', visited = [], double = False, path = []):
    if pos == 'end':
        path.append(pos)
        print(','.join(path))
        return 1
    if pos in visited:
        if double or pos == 'start': return 0
        double = True

    if pos.islower():
        visited.append(pos)
    path.append(pos)

    return sum(pathfind2(next, visited.copy(), double, path.copy()) for next in paths[pos])

# print(paths)
print(pathfind2())
