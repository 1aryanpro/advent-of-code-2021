input = open("inputs/day4.txt", "r").readlines()
draws = [int(n) for n in input[0].split(",")]

input = input[2:]

boards = [[]]
marks = [[]]

for line in input:
    if line == "":
        boards.append([])
        marks.append([])
        continue
    boards[-1].append([int(n) for n in line.split()])
    marks[-1].append([False for _ in range(5)])


def markNum(num, board, mark):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                mark[i][j] = True


def checkWin(mark):
    rows = [0] * 5
    cols = [0] * 5
    for i in range(5):
        for j in range(5):
            if mark[i][j]:
                rows[j] += 1
                cols[i] += 1
    return 5 in rows or 5 in cols


def calcScore(board, mark):
    total = 0
    for i in range(5):
        for j in range(5):
            if mark[i][j]:
                continue
            total += board[i][j]
    return total


# Part 1
winner = -1
lastNum1 = -1
for draw in draws:
    for i in range(len(boards)):
        markNum(draw, boards[i], marks[i])
        if checkWin(marks[i]):
            winner = i
            lastNum1 = draw
            break
    if winner != -1:
        break
print(calcScore(boards[winner], marks[winner]) * lastNum1)


# Part 2
winners = []
lastNum2 = -1
for draw in draws:
    for i in range(len(boards)):
        if i in winners:
            continue
        markNum(draw, boards[i], marks[i])
        if checkWin(marks[i]):
            winners.append(i)
            lastNum2 = draw

loser = winners[-1]
print(calcScore(boards[loser], marks[loser]) * lastNum2)
