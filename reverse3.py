# pgm to print the given string object from the end in reverse order

s=input("Enter the string: ")  # user input
l=s.split()  # spliting the given string
i=len(l)-1
l1=[]
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output)  # printing the output
