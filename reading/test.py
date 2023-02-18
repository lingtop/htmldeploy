lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2=[]
num=10
for i in range(len(lst)):
  if lst[i]+lst[-i-1]==num:
    lst2.append(lst[i])
    lst2.append(lst[-i-1])
print(lst2)