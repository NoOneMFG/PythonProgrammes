L  = int(input())
S  = int(input())
D = S - L
if D <= 0:
  print("Congratulations, you are within the speed limit!")
else:
  if D <= 20:
    Fine = "$100"
  elif D <= 30:
    Fine = "$270"
  else:
    Fine = "$500"
  print("You are speeding and your fine is " + Fine + ".")
