h = int(input())
M = int(input())
c = 0
for i in range(M):
    t = i+1
    A = h*(t**3) + 2*(t**2) + t - 6*(t**4)
    if A <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        c += 1
        break
if c == 0:
    print("The balloon does not touch ground in the given time.")