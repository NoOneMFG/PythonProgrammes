inp = input()
le = ["I", "O", "S", "H", "Z", "X", "N"]
ln = len(inp)
count = 0
for x in inp:
    for i in le:
        if x == i:
            count += 1
if ln == count:
    print("YES")
else:
    print("NO")