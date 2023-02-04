input = open("inputs/day10.txt").readlines()
code = [l[:-1] for l in input]

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

corruptPoints = [3, 57, 1197, 25137]
incompletePoints = [1, 2, 3, 4]

combos = dict(zip(closings, openings))
cPointValues = dict(zip(closings, corruptPoints))
iPointValues = dict(zip(openings, incompletePoints))


def parseCorruptLine(line):
    opens = []
    for c in line:
        if c in openings:
            opens.append(c)
            continue
        if combos[c] != opens.pop():
            return cPointValues[c]
    return 0


def parseIncompleteLine(line):
    opens = []
    for c in line:
        if c in openings:
            opens.append(c)
            continue
        if combos[c] != opens.pop():
            return 0

    out = 0
    while opens:
        out = 5 * out + iPointValues[opens.pop()]
    return out


scores = []
for line in code:
    score = parseIncompleteLine(line)
    if score != 0:
        scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
