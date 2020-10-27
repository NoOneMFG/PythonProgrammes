a = int(input())
b = int(input())
c = int(input())
if a > 100:
  pa = round((a - 100) * 0.25 + b * 0.15 + c * 0.20, 2)
else:
  pa = round(b * 0.15 + c * 0.20, 2)

if a > 250:
  pb = round((a - 250) * 0.45+b*0.35+c*0.25, 2)
else:
  pb = round(b*0.35+c*0.25, 2)
print("Plan A costs " + str(pa))
print("Plan B costs " + str(pb))
if pa > pb:
  print("Plan B is cheapest.")
elif pa < pb:
  print("Plan A is cheapest.")
else:
  print("Plan A and B are the same price.")