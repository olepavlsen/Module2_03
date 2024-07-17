list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = len(list)
a = 0
while True:
    num = list[a]
    if num > 0:
        print(num)
    a = a + 1
    if num < 0 or a > n-1:
        break
