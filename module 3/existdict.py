d = {'apple': 10, 'banana': 5, 'orange': 8}

check = 'banana'

if check in d:
    print(f"The key '{check}' exists in the dictionary with value {d[check]}.")
else:
    print(f"The key '{check}' does not exist in the dictionary.")
