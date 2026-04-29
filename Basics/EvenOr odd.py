# Program to check whether a number is Even or Odd
def check_even_odd(n):  #Function to check even r odd
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

n=int(input("Enter the number: "))
result=check_even_odd(n)
