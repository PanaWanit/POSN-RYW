n = 10
i = 0
while i < n:
    j = 0
    while j < n:
        if j < i + 1:
            print("y", end="")
        else:
            print("x", end="")
        j += 1
    print()
    i += 1
