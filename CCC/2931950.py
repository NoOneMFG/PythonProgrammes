N = int(input())
k = int(input())
i = 1
while i < k:
  N += N * 10**i
  i += 1
print(N)