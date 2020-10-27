w = int(input())
h = float(input())

bmi = w / h**2
if 25 >= bmi >= 18.5:
  print("Normal weight")
elif bmi > 25:
  print("Overweight")
else:
  print("Underweight")