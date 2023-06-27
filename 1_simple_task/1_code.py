n = int(input())
x = 2
N = ""
while n != 1:
    if n % x == 0:
        if n != x:
            N = N + str(x) + ' * '
            n = n // x  
        if n == x:
            N = N + str(x) 
            n = n // x
    elif n % x != 0:
        x = x + 1
print(N)