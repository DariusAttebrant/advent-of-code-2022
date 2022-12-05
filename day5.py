from copy import deepcopy

file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday5.txt')
data = file.read().split('\n\n')
numberofstacks = 9
maxheightofstacks = 8

# skapar lista i lista av ursprungskonfigurationen
config = []
orders = data[1]
print(data[0])
for j in range(8):
    for i in range(1, 8 * 4 * numberofstacks, 4):
        config.append(data[0][i])

conf2 = []
for i in range(numberofstacks):
    phlist = []
    for j in range(0, maxheightofstacks * numberofstacks, numberofstacks):
        if config[j + i] != ' ':
            phlist.append(config[j + i])
    phlist.reverse()
    conf2.append(phlist)

# städar upp ordningskommandon

cmdlist = orders.split('\n')
for i in range(len(cmdlist)):
    cmdlist[i] = cmdlist[i].split()
    cmdlist[i].remove('move')
    cmdlist[i].remove('from')
    cmdlist[i].remove('to')

# utför orders
conf21 = deepcopy(conf2)

def movecrate(quantity, startpos, endpos):
    conf3 = conf21
    for i in range(quantity):
        conf3[endpos - 1].append(conf3[startpos - 1].pop())
    return conf3


for i in range(len(cmdlist)):
    conf21 = movecrate(int(cmdlist[i][0]), int(cmdlist[i][1]), int(cmdlist[i][2]))

# kompilerar slutgiltigt svar
ans = ''
for i in range(numberofstacks):
    ans += conf21[i][len(conf21[i]) - 1]

print('1) final crate on top of each stack after rearrangement:', ans)

# ---------------------------------------- 2 ----------------------------------------------------------
conf22 = deepcopy(conf2)
def movecrate2(quantity, startpos, endpos):
    conf3 = conf22
    for i in range(quantity):
        conf3[endpos - 1].append(conf3[startpos - 1].pop(len(conf3[startpos - 1]) - quantity + i))

    return conf3

for i in range(len(cmdlist)):
    conf22 = movecrate2(int(cmdlist[i][0]), int(cmdlist[i][1]), int(cmdlist[i][2]))

# kompilerar slutgiltigt svar

ans2 = ''
for i in range(numberofstacks):
    ans2 += conf22[i][len(conf22[i]) - 1]

print('2) final crate on top of each stack after rearrangement:', ans2)