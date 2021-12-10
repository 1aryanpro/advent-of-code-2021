input = open('inputs/day8.txt').readlines()
input = [l.split(" | ") for l in input]

hints = [sorted(e[0].split(), key = len) for e in input]
codes = [e[1].split() for e in input]

for i in range(len(hints)):
    for j in range(len(hints[i])):
        hints[i][j] = set(hints[i][j])
    for j in range(len(codes[i])):
        codes[i][j] = set(codes[i][j])


count = 0
for ln in range(len(hints)):
    hint = hints[ln]
    code = codes[ln]
    decode = [{} for i in range(10)]

    decode[1] = hint[0]
    decode[7] = hint[1]
    decode[4] = hint[2]
    decode[8] = hint[9]

    output = ""
    
    for n in range(3, 6):
        curr = hint[n]
        if decode[7].issubset(curr): decode[3] = curr
        elif (decode[4] - decode[1]).issubset(curr): decode[5] = curr
        else: decode[2] = curr

    for n in range(6, 9):
        curr = hint[n]
        if decode[4].issubset(curr): decode[9] = curr
        elif decode[1].issubset(curr): decode[0] = curr
        else: decode[6] = curr

    for n in code:
        output += str(decode.index(n))

    count += int(output)
print(count)

# for i in codes:
#     line = codes[i]
#     for digit in line:
#         if len(digit) in [2, 3, 4, 7]: count += 1
# print(count)

