fy = int(input())
sy = int(input())

may = []
tres = []
prog = []
dcat = []
el = int(fy)
i = 0
while el < sy:
    may.append(i*4+fy)
    tres.append(i*2+fy)
    prog.append(i*3+fy)
    dcat.append(i*5+fy)
    if i*2+fy > sy-2:
        break
    el += 1
    i += 1
common = set(may) & set(tres) & set(prog) & set(dcat)
com = list(common)
com.sort()
if len(com) == 0:
    print("All positions change in year",fy)
else:
    for x in com:
        print("All positions change in year",x)