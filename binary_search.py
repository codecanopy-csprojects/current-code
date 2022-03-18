barlist = [1, 5, 10, 15, 20]
target = 2

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

print(found)
