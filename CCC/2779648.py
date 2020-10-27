N = int(input())
k = int(input())
s = N
for i in range(1, k):
 s += N*(10**i)print(s)