i = ["A", "B", "C", "D", "E"]
b = 6
while b != 4:
    b = int(input())
    n = int(input())
    if b == 4:
        break
    elif b == 1:
        for x in range(n):
            i = [i[1], i[2], i[3], i[4], i[0]]
    elif b == 2:
        for x in range(n):
            i = [i[4], i[0], i[1], i[2], i[3]]
    else:
        for x in range(n):
            i = [i[1], i[0], i[2], i[3], i[4]]
print(i[0], i[1], i[2], i[3], i[4])