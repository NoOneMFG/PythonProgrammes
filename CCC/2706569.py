import re
x = input()
y = input()
t = int(input())

c1 = [int(d) for d in re.findall(r'-?\d+', x)]
c2 = [int(d) for d in re.findall(r'-?\d+', y)]

tot = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
oe = tot % 2
tc = t % 2

if tot > t:
    print("N")
elif oe == tc:
    print("Y")
else:
    print("N")