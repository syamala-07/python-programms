n=4
for i in range(1,n+1):
    print(" "*(n-1), end=" ")
    for j in range(i):
        print("*",end="  ")
    print()