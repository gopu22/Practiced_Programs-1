# pgm to print multiple of n nos. from 1 to n pattern

n=int(input("Enter the number: "))  # user input
for i in range(1,n+1):  # i loop for rows
    for j in range(i):  # j loop in range of i
        print("* "*i)  # printing output
    print()
