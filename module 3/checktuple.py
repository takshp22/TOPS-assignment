t = (1, 2, 3, 4, 5)
check = 9
found = False

for item in t:
    if item == check:
        found = True
        break

if found:
    print("Element", check, "exists within the tuple.")
else:
    print("Element", check, "does not exist within the tuple.")
