print("======temp calculator======")
print("1.c to f ")
print("2.f to c ")
print("3.c to k ")
num = int(input("select :"))
if num == 1:
    print("======c to f======")
    c = float(input("enter c :"))
    f = (c*9/5)+32
    print(f"Temp in f = {f:.2f} f")
elif num == 2:
    print("======f to c======")
    f = float(input("enter f :"))
    c = (f-32)*5/9
    print(f"temp in c = {c:.2f} c")
elif num == 3:
    print("======c to k======")
    c = float(input("enter c :"))
    k = c+273.15
    print(f"temp in k = {k:.2f} k")
else:
    print("error")
