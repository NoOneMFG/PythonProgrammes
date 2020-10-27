w = input()
re = list(w)

def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
def closec(s):
    if s == "z":
        return "z"
    elif any(alp[alp.index(s)+1] == alp[vow[x]] for x in range(len(vow))):
        return alp[alp.index(s)+2]
    else:
        return alp[alp.index(s)+1]

alp = list("abcdefghijklmnopqrstuvwxyz")
vow = [0, 4, 8, 14, 20]
wcon = list()
for i in range(len(w)):
    if any(w[i] == alp[vow[x]] for x in range(len(vow))):
        continue
    else:
        wcon.append(w[i])

for i in range(len(wcon)):
    cv = alp[closest(vow, alp.index(wcon[i]))]
    cc = closec(wcon[i])
    re[re.index(wcon[i])] = wcon[i] + cv + cc
res = ""
for i in range(len(re)):
    res = res + re[i]
print(res)