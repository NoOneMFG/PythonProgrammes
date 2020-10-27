value = int(input())
factors = []
diff = 10000000
sp = list()
for i in range(1, int(value**0.5)+1): 
    if value % i == 0: 
        factors.append((i, int(value / i)))
        if int(value/i) - i < diff:
            sp = [i, int(value / i)]
peri = (sp[0] + sp[1]) * 2
text = "Minimum perimeter is " + str(peri) + " with dimensions " + str(sp[0]) + " x " + str(sp[1])
print(text)