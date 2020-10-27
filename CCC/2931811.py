x = [1, 2, 3, 4]
x[0] = int(input())
x[1] = int(input())
x[2] = int(input())
x[3] = int(input())

y = sorted(x)
z = sorted(x, reverse=True)

if x == y:
    print("Fish Rising")
elif x == z:
    print("Fish Diving")
elif x[0] == x[1] == x[2] == x[3]:
    print("Constant Depth")
else:
    print("No Fish.")