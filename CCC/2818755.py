import re
k = int(input())
codes = list()
for n in range(k):
    x = input()
    codes.append([x.split()[0], x.split()[1]])
toEncode = input()
while re.findall(r'\d+', toEncode) != []:
    for i in codes:
        if toEncode.replace(i[1], i[0], 1) != toEncode:
            toEncode = toEncode.replace(i[1], i[0], 1)
            break
print(toEncode)