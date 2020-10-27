n = int(input())
an = 100
da = 100
for i in range(n):
    a = input()
    r = [int(s) for s in a.split() if s.isdigit()]
    if r[0] > r[1]:
        da = da - r[0]
    elif r[0] < r[1]:
        an = an - r[1]
    else:
        continue
print(an)
print(da)