#lst = [6, 2, 1, 8, 10]
lst = [1,1,11,2,3]
lst = sorted(lst)
lst.pop(0)
lst.pop(len(lst) - 1)
print(sum(lst))