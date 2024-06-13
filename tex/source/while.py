i = 2
while i < 5:
    print(i, end=" ")  # 2 3 4
    i += 1

i = 4
while i >= 2:
    print(i, end=" ")  # 4 3 2
    i -= 1

i = 1
while i < 32:
    print(i, end=" ")
    i = 2 * i + 1  # 1 3 7 15 31
