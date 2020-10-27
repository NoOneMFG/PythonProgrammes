x = int(input())
y = int(input())

n = int(x)
count = 0
while n < y+1:
    fac = []
    for i in range(1, n+1):
        if n % i == 0:
            fac.append(i)
    if len(fac) == 4:
        count += 1
    n += 1
print("The number of RSA numbers between ",x," and ",y," is ", count)