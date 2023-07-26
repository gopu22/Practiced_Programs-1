# program to print sum of n nos.

n=int(input("Enter the n numbers: "))  # user input
sum=0
i=1
while i<=n:  # while condition
    sum=sum+i  # incrementing sum by adding i to it
    i+=1  # incrementing i with 1 in every loop
print("The sum of first",n,"numbers is: ", sum)  # printing the output

