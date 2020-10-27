fy = int(input())
sy = int(input())

diff = sy - fy
yrs = []
x = [n for n in range(0, diff) if n % 60 == 0]
i = 0
while i < len(x):
    print("All positions change in year " +str(fy+x[i]))
    i += 1