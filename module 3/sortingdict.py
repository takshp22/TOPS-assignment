d = {'apple': 10, 'banana': 5, 'orange': 8}

asc = dict(sorted(d.items(), key=lambda item: item[1]))
desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", asc)
print("Descending order:", desc)
