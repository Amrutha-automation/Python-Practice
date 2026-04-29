# plaindrome check for string
def palindrome(s):
    s=str(s)
    return s==s[::-1]

s=input("Enter the string: ")
if palindrome(s):
    print("it is palindrome")
else:
    print("it is not palindrome")

# plaindrome check for numbers
def palindrome(n):
    original = n
    reverse_n = 0

    while n > 0:
        digit= n%10
        reverse_n = reverse_n*10+digit
        n//=10
    return original == reverse_n

n=int(input("Enter the number: "))
if palindrome(n):
    print("it is palindrome")
else:
    print("it is not palindrome")
