N = int(input())

fCount = 0
eCount = 0

psg = str()
for i in range(N):
    txt = input()
    psg = psg + txt

if psg.count('t') + psg.count('T') > psg.count('s') + psg.count('S'):
    print('English')
else:
    print('French')
