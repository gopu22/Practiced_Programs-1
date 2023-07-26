# pgm to print the string in reverse order

s=input("Enter the string: ")  # user string input
print(''.join(reversed(s)))  # printing the output using reversed() function
#  OR
print(s[::-1])  # printing the output using slicing method
