n = [5, 2, 8, 1, 9, 3, 7, 4]

s = second_smallest = float('inf')

for i in n:
    if i < s:
        second_smallest = s
        s = i
    elif i < second_smallest and i != s:
        second_smallest = i

print("Second smallest number:", second_smallest)
