input = open('inputs/day3.txt', 'r').readlines()
arr = [y for y in input]
size = len(arr[0])
counts = [0]*size

for n in arr:
    for i in range(size):
        if n[i] == '1':
            counts[i] += 1
        else:
            counts[i] -= 1

bcounts = ['1' if n > 0 else '0' for n in counts]

gamma = "".join(['1' if n >  0 else '0' for n in counts])
epsil = "".join(['1' if n <= 0 else '0' for n in counts])

O2arr  = arr
CO2arr = arr

for i in range(size):
    O2bit = 0
    for n in O2arr:
        if n[i] == '1':
            O2bit += 1
        else:
            O2bit -= 1
    O2bit = '1' if O2bit >= 0 else '0'

    CO2bit = 0
    for n in CO2arr:
        if n[i] == '1':
            CO2bit += 1
        else:
            CO2bit -= 1
    CO2bit = '1' if CO2bit < 0 else '0'

    if len(O2arr) > 1:  O2arr  = list(filter(lambda n: O2bit  == n[i], O2arr))
    if len(CO2arr) > 1: CO2arr = list(filter(lambda n: CO2bit == n[i], CO2arr))

print(O2arr[0], CO2arr[0])
print(int(O2arr[0], 2) * int(CO2arr[0], 2))
