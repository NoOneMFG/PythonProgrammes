t = int(input())
s = int(input())
h = int(input())
i = 1
while i < t+1:
  print("*" + " " * s + "*" + " " * s + "*")
  i += 1
print("*" * (3 + s * 2))
q = 1
while q < h+1:
  print(" " * (s+1) + "*")
  q += 1