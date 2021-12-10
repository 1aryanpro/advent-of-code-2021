input = open('inputs/day6.txt', 'r').readlines()
input = input[0].split(',')
input = list(map(int, input))

school = [0]*9
for fish in input: school[fish] += 1

for day in range(256):
    newborn = school[0]

    for age in range(len(school) - 1):
        school[age] = school[age + 1]

    school[8] = newborn
    school[6] += newborn

print(school)
print(sum(school))


