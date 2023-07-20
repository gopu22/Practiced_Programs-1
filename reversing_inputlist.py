# program to sort the two input array's into single output array.

a=input("enter the list a: ")  # user input 'a'
b=input("enter the list b: ")  # user input 'b'
add=a+b  # adding 'a' and 'b'
print(add)  # printing the added value
print(sorted(add))  # sorting the added values
reverse=add[::-1]   # reversing the sorted array
print(reverse)  # printing the reversed array


