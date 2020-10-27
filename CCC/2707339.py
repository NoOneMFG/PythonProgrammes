sqr = 1
obs = [[54, 19], [90, 48], [99, 77], [9, 34], [40, 64], [67, 86]]
while sqr > 0:
  x = int(input())
  if x < 1:
    print("You Quit!")
    break
  else:
    if (sqr + x) <= 100:
      sqr = sqr + x
    for n in obs:
      if sqr == n[0]:
        sqr = n[1]
        break
  print("You are now on square", sqr)
  if sqr == 100:
      print("You Win!")
      break