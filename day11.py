input = open('inputs/day11.txt').readlines()
input = [[int(i) for i in line[:-1]] for line in input]

def printInput():
    for l in input:
        print(''.join(str(c) for c in l))
    print('')

h = len(input)
w = len(input[0])

def incAll():
    for i in range(h):
        for j in range(w):
            input[i][j] += 1

def flashAll():
    out = 0
    for i in range(h):
        for j in range(w):
            if(input[i][j] > 9):
                out += flash(i, j)
    return out

def flash(y, x):
    out = 1
    input[y][x] = 0
    for i in range(max(0, y-1), min(h, y+2)):
        for j in range(max(0, x-1), min(w, x+2)):
            if input[i][j] == 0: continue
            input[i][j] += 1
            if input[i][j] > 9:
                out += flash(i, j)
    return out

def doStep():
    incAll()
    return flashAll()

# count = 0
# for i in range(100):
#     count += doStep()
# print(count)

i = numFlashes = 0
while numFlashes != w*h:
    numFlashes = doStep()
    i += 1
print(i)
