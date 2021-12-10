input = open('inputs/day7.txt', 'r').read().split(',')
input = [int(x) for x in input]
print(input)

# positions = {}
#
# for x in input:
#     if x in positions:
#         positions[x] += 1
#     else:
#         positions[x] = 1
#
# print(positions)


# middlePos = int(len(input)/2)
# finalPos = input[middlePos]
# fuelUsed = sum([abs(x - finalPos) for x in positions])

def resum(n): return int(n*(n+1)/2)
def fuelUsed(n): return sum([resum(abs(x - n)) for x in input])

fuelUsages = [fuelUsed(p) for p in range(max(input))]

print(min(fuelUsages))
