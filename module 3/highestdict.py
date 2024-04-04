d = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

# Sort the dictionary items by values in descending order
sort = sorted(d.items(), key=lambda item: item[1], reverse=True)

# Extract the highest 3 values
highest = sort[:3]

# Print the highest 3 values
print("Highest 3 values in the dictionary:")
for key, value in highest:
    print(key, ":", value)
