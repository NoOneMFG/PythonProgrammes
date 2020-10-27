Pink = int(input())
Green = int(input())
Red = int(input())
Orange = int(input())
toRaise = int(input())
to = toRaise + 1
count = 0
mini = 9999999
for i in range(to):
    for j in range(to):
        for k in range(to):
            for l in range(to):
                res = i*Pink + j*Green + k*Red + l*Orange
                totTicks = i + j + k + l
                if i == j == k == 0:
                    continue
                if mini > totTicks:
                    mini = totTicks
                if res == toRaise:
                    print("# of PINK is", i , "# of GREEN is", j ,"# of RED is", k ,"# of ORANGE is ", l)
                    count += 1
print("Total combinations is ", count, ".", sep="")
print("Minimum number of tickets to print is ", mini, ".", sep="")