i = 0
n = 0
while i < 6:
  inp = input()
  if inp == "W":
    n += 1 
  i += 1
if n > 4:
  print("1")
if n == 4 or n == 3:
  print("2")
if n == 1 or n == 2:
  print("3")
if n == 0:
  print("-1")