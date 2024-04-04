dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 30, 'c': 40, 'd': 50}

dict3 = {}

for key in dict1.keys() | dict2.keys():
    dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)

print("Combined Dictionary:",dict3)
