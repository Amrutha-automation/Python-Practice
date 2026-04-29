#Example1:Checking even or Odd my directly pasing inputs
# #n= 28
#if n % 2 == 0:
#    print("Number is even")
#else:
#    print("Number is odd")



# Example 2: To take inputs from users
def check_even_odd(n):  #Function to check even r odd
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

n=int(input("Enter the number: "))
result=check_even_odd(n)
