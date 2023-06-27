n = int(input())
m = int(input())
x = len(str(n * m))
count = 1
q = 1
for i in range(1, (m * n) + 1):
    if count % 2 != 0:
        if i % m == 0:
            print((" " * (x - len(str(i)))) + str(i))
            count += 1
            continue
        else:
            print((" " * (x - len(str(i)))) + str(i), end=' ')
    if count % 2 == 0:
        if (i + m - q - 1) % m == 0:
            print((" " * (x - len(str(i + m - q)))) + str(i + m - q))
            count += 1
            q = 1
            continue
        else:
            print((" " * (x - len(str(i + m - q)))) + str(i + m - q), end=' ')
            q += 2