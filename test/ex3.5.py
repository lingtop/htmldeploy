list1 = [10, 15, 20, 22, 24, 3, 7]
def is_even(num):
    list2=[]
    for x in list1 :
        if x %2==0:
            list2.append(x)
    print(f'เลขคู่มี{len(list2)} ตัวคือ {list2}')           
is_even(list1)