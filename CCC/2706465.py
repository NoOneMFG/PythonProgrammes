to = int(input())
v = input()
a = 0
b = 0
for x in v:
    if x == "A":
        a += 1
    elif x == "B":
        b += 1
if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")