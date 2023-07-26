# pgm to print increase & decrease of a given number in order wise

n=int(input("Enter the number: "))  # user input
for i in range(1,n+1):  # i loop for rows
    for j in range(i):  # j loop in range of i
        print("* ",end=" ")  # printing output
    print()

for k in range(1,n+1):  # k loop for rows
    for l in range(n+1-k):  # l loop in range of n+1-k
        print("* ",end=" ")  # printing output
    print()
