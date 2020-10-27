x = [1, 2, 3, 4]
x[0] = int(input())
x[1] = int(input())
x[2] = int(input())
x[3] = int(input())

if x[0] == x[1] == x[2] == x[3]:
    print("Fish At Constant Depth")
elif x[0] < x[1] < x[2] < x[3]:
    print("Fish Rising")
elif x[0] > x[1] > x[2] > x[3]
    print("Fish Diving")
else:
    print("No Fish")
