inp = input()

hap = [i for i in range(len(inp)) if inp.startswith(":-)", i)] 
sad = [i for i in range(len(inp)) if inp.startswith(":-(", i)] 

if len(hap) > len(sad):
    print("happy")
elif len(hap) < len(sad):
    print("sad")
elif len(hap) == len(sad) == 0:
    print("none")
elif len(hap) == len(sad):
    print("unsure")
else:
    print("none")