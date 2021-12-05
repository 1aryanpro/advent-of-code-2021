input = open('inputs/day1.txt', 'r').read().split('\n')
arr = [int(y) for y in input[:-1]]
count1 = count2 = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        count1 += 1

for i in range(3, len(arr)):
    if arr[i] > arr[i-3]:
        count2 += 1

print(f"{count1 = }")
print(f"{count2 = }")
