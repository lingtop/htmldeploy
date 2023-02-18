x=input("num :")
list1 = []
for y in x : 
    list1.append(int(y))
    print(f'{y}+',end="") if y != x[len(x)-1] else  print(y,end="")
print(f' = {sum(list1)}')
