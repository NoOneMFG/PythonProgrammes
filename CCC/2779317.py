x = input()
y = input()
t = int(input())

c1 = [int(s) for s in x.split() if s.isdigit()]
c2 = [int(s) for s in y.split() if s.isdigit()]

tot = abs(c1[0]-c1[1]) + abs(c2[0]-c2[1])
oe = tot % 2
tc = t % 2

if tot > t:
    print("N")
elif oe == tc:
    print("Y")
else:
    print("N")