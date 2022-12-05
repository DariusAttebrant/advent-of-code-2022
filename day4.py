file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday4.txt')
data = file.read().split('\n')
containcount = 0
overlapcount = 0
def contained(elf1, elf2):
    if (elf1[1] <= elf2[1]) & (elf1[0] >= elf2[0]):
        return True
    if (elf1[1] >= elf2[1]) & (elf1[0] <= elf2[0]):
        return True

def overlap(elf1, elf2):
    if (elf1[1] < elf2[0]) | (elf2[1] < elf1[0]):
        return False
    else:
        return True


for i in range(len(data)):
    row = data[i].split(',')
    elf1 = list(map(int, row[0].split('-')))
    elf2 = list(map(int, row[1].split('-')))
    if overlap(elf1, elf2):
        overlapcount += 1
    if contained(elf1, elf2):
        containcount += 1

print('1) number of contained pairs =', containcount)

print('1) number of pairs with overlap =', overlapcount)