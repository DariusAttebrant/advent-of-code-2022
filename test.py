file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday3.txt')

value = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priosum = 0
gpriosum = 0

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
            if comp1[k] == comp2[l] and comp1[k] not in sims:
                sims += comp1[k]
    return sims

gpriosum = findvalue(similarities())
print(similarities())
print(findvalue(similarities()))
print(findvalue())
print(gpriosum)