N = int(input())
k = int(input())

s = N
for i in range(k):
    t = i+1
    s += N*(10**t)
print(s)