num = [10, 5, 20, 8, 15]
l = num[0]
s = num[0]
sum = 0

for num in num:
    if num > l:
        l = num
    if num < s:
        s = num
    sum += num

print("Largest number:", l)
print("Smallest number:", s)
print("Sum of all numbers:", sum)
