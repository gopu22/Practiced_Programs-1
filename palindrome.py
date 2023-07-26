# palindrome program

n=input("Enter the number: ")  # taking input from user and storing it in 'n'
reverse=n[::-1]  # reversing variable 'n'
if reverse==n:   # if condition
    print("It is a palindrome")
else:
    print("It is not a palindrome")

