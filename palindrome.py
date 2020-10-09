#To find whether a given number is palindrome or not


print("Enter the number you wish to check ")

numb = int(input())


temp = numb

reverse = 0


while(numb>0):

    digit = numb%10

    reverse = reverse*10 + digit

    numb = numb//10


if(temp==reverse):

    print("The number is a palindrome")


else:

    print("The number is not a palindrome")