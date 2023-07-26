# pgm to reverse only the elements objects in the given string

s=input('Enter the string: ')  # user input
l=s.split()
l1=[]
for x in l:
    l1.append(x[::-1])
    output=' '.join(l1)
print(output)  # printing the output
