def FactorialRecurssion(n):
   if n==0 or n==1:
       return 1
   return n*FactorialRecurssion(n-1)


n=int(input("Enter the number: "))
print(f"Factorial of {n} is: {FactorialRecurssion(n)}")
