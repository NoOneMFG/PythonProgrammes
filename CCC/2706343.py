tr = int(input())
pk = int(input())
pc = int(input())
tot = int(input())
to = tot + 1
count = 0
for i in range(to):
    for j in range(to):
        for k in range(to):
            res = i*tr + j*pk + k*pc
            if i == j == k == 0:
                continue
            if res <= tot:
                print(i, "Brown Trout,",j,"Northern Pike,",k,"Yellow Pickerel")
                count += 1
print("Number of ways to catch fish:", count)