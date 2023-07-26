# pgm to print the string in reverse format

s=input("enter the string: ")  # user string input
i=len(s)-1
output=''
while i>=0:
    output=output+s[i]
    i=i-1
print(output)  # printing the output
