# Program to find factorial of a number
def Factorial(n):
    result=1
    for i in range (1,n+1):
        result*=i
    return result

n=int(input("Enter the number: "))
print(f"Factorial of {n} is: {Factorial(n)}")
