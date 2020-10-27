a = input()
b = input()
c = input()
d = input()
r1 = [int(s) for s in a.split() if s.isdigit()]
r2 = [int(s) for s in b.split() if s.isdigit()]
r3 = [int(s) for s in c.split() if s.isdigit()]
r4 = [int(s) for s in d.split() if s.isdigit()]

s = [r1, r2, r3, r4]
c1 = []
c2 = []
c3 = []
c4 = []
for i in range(4):
    c1.insert(i ,s[i][0])
for i in range(4):
    c2.insert(i, s[i][1])
for i in range(4):
    c3.insert(i, s[i][2])
for i in range(4):
    c4.insert(i, s[i][3])
if sum(r1) == sum(r2) == sum(r3) == sum(r4) == sum(c1) == sum(c2)  == sum(c3)  == sum(c4):
    print("magic")
else:
    print("not magic")

