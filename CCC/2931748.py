n  = int(input())

if n < 6:
  print(n-1)
else:
  if n == 6:
    print(3)
  elif n == 8 or n == 7:
    print(2)
  else:
    print(1)