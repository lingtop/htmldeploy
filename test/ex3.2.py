num=[2, 3, 1, 5, 9, 24, 10]
max=num[0]
min=num[0]
for x in num :
    if x<min :
        min=x
    if x>max :
        max=x
print(min)
print(max)