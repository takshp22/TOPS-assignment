s = ['level', 'hello', 'radar', 'python', 'pop', 'wow', 'ab', 'a']

count = 0

for i in s:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("Number of strings:", count)
