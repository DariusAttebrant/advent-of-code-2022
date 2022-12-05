file = open(r'C:\Users\warthog\Documents\Skola\code\advent of code 2022\inputday1.txt')
list1 = file.read().split('\n\n')
for i in range(len(list1)):
    list1[i] = list1[i].split('\n')
    for j in range(len(list1[i])):
        list1[i][j] = int(list1[i][j])
list2 = [0] * len(list1)
print(list2)
for i in range(len(list1)):
    for j in range(len(list1[i])):
        list2[i] += list1[i][j]
list2.sort(reverse = True)
print(list2)
print(list2[0])
print(list2[0] + list2[1] + list2[2])
