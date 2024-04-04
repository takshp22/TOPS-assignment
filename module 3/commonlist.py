l1=[1,2,3,4,5]
l2=[0,6,7,8,9]
result = False
for x in l1:
    for y in l2:
        if x==y:
            result = True
            print(result)
if result:
   print("List have at least one common member")
else:
   print("List do not have any commom member")
