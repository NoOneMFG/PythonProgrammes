n  = int(input())
if n == 1:
  print(1)
elif n < 5:
  print(n-1)
else:
  if n == 6 or n == 5:
    print(3)
  elif n == 8 or n == 7:
    print(2)
  else:
    print(1)