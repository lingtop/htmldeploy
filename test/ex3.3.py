n = int(input("Enter num: "))
list = [str(num) for num in range(n, 0, -1)]
print(f"{n}! = ", end="")
print('x'.join(list), end="")
result = 1
for num in list:
  result *= int(num)
print(f"= {result}")

