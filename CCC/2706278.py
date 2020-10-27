m = int(input())
n = int(input())
count = 0
i = 1
while i < m+1:
    t = 1
    while t < n+1:
        if i + t == 10:
            count += 1
        t += 1
    i += 1
if count == 1:
    print("There is 1 way to get the sum 10.")
elif count == 0:
    print("There are 0 ways to get the sum 10.")
else:
    print("There are",count,"ways to get the sum 10.")