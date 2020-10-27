k = int(input())
codes = list()
for n in range(k):
    x = input()
    codes.append([x.split()[0], x.split()[1]])
toEncode = input()
for i in codes:
    toEncode = toEncode.replace(i[1], i[0])
print(toEncode)