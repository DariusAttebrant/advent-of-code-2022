# A rock       1
# B paper      2
# C scissor    3
# X lose
# Y draw
# Z win
def score(row):
    row = row
    ABC = [1, 2, 3]
    if row[0] == 'A' and row[1] == 'X':
        return 3 + 0
    elif row[0] == 'A' and row[1] == 'Y':
        return 1 + 3
    elif row[0] == 'A' and row[1] == 'Z':
        return 2 + 6   

    elif row[0] == 'B' and row[1] == 'X':
        return 1 + 0
    elif row[0] == 'B' and row[1] == 'Y':
        return 2 + 3
    elif row[0] == 'B' and row[1] == 'Z':
        return 3 + 6        

    elif row[0] == 'C' and row[1] == 'X':
        return 2 + 0
    elif row[0] == 'C' and row[1] == 'Y':
        return 3 + 3
    elif row[0] == 'C' and row[1] == 'Z':
        return 1 + 6
    else:
        print('xd')
        return 0


file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday2.txt')
data = file.read().split('\n')
points = 0



for i in range(len(data)):
    data[i] = data[i].split()
    points += int(score(data[i]))
print('total points =', points)
