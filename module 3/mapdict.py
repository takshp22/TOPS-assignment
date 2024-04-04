keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = {}

for key, value in zip(keys, values):
    d[key] = value

print("Mapped Dictionary:", d)
