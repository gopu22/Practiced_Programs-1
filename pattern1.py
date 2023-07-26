# program to print right angle triangle pattern

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):  # i represents row number
    for j in range(i):  # j represents the number of loops to print '*'
        print("* ", end=" ")
    print()

