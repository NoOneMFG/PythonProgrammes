N = int(input())
k = int(input())

s = N
for i in range(1, k+1):
    s += N*(10**i)
print(s)