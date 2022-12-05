file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday3.txt')
value = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priosum = 0

def findvalue(char):
    val = 0
    for i in range(len(value)):
        if value[i] in char:
            val += i + 1
    return val

def similarities(comp1, comp2, comp3):
    sims = ''
    for k in range(len(comp1)):
        for l in range(len(comp2)):
            for n in range(len(comp3)):
                if comp1[k] == comp2[l] == comp3[n] and comp1[k] not in sims:
                    sims += comp1[k]
    return sims

data = file.read().split('\n')

for j in range(len(data)):
    comp1 = data[j][slice(0, len(data[j]) // 2)]
    comp2 = data[j][slice(len(data[j]) // 2, len(data[j]))]
    priosum += findvalue(similarities(comp1, comp2, value))

print('1) sum of priorities =', priosum)

# -------------------------------- 2 -------------------------------------- #

gpriosum = 0

for j in range(len(data)):
    if j % 3 == 0:
        comp1 = data[j]
        comp2 = data[j + 1]
        comp3 = data[j + 2]
        gpriosum += findvalue(similarities(comp1, comp2, comp3))

print('2) groupwise sum of priority badges', gpriosum)