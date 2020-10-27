x = int(input())
y = int(input())
z = int(input())
d = int(input())
s = int(input())

def find(a, b):
  n = s // (a+b)
  ni = s % (a+b)
  if a < ni:
    return n*(a-b) - (ni-a)
  else:
    return n*(a-b) + ni

nik = find(x,y)
byr = find(z,d)
if nik > byr:
  print("Nikky")
if nik == byr:
  print("Tied")
else:
  print("Byron")