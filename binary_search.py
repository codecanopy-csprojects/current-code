def binary_search(barlist, target):
    start = 0
    end = len(barlist) - 1
    found = False
    while not found and start <= end:
        mid = (start + end) // 2
        if target == barlist[mid]:
            found = True
        elif target < barlist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return found


barlist1 = [13, 16, 19, 20, 21, 27, 30]
print(binary_search(barlist1, 20))
print(binary_search(barlist1, 13))
print(binary_search(barlist1, 30))
print(binary_search(barlist1, 35))

barlist2 = ["Monty", "Python", "Thelma", "Louise", "Bonnie", "Clyde"]
print(binary_search(barlist2, "Monty"))
print(binary_search(barlist2, "Thelma"))
print(binary_search(barlist2, "Stella"))
print(binary_search(barlist2, "Greg"))
