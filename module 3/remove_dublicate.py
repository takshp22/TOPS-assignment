l = [1, 2, 3, 4, 2, 3, 5, 6, 7, 7, 8, 9, 1]
l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print("List with duplicates removed:", l1)
