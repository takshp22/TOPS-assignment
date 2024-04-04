l = [1, 2, 3, 4, 2, 3, 5, 6, 7,8,1]

unique = []

# Loop through the list
for item in l:
    if item not in unique:
        unique.append(item)

print("Unique values:", unique)
