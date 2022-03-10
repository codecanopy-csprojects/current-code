barlist = [6, 5, 4, 3, 2, 1]

for i in range(1, len(barlist)):
    insert = barlist[i]
    index = i
    while index > 0 and insert < barlist[index-1]:
        barlist[index] = barlist[index-1]
        index -= 1
    barlist[index] = insert

print(barlist)
