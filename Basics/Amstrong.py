# Program to check Armstrong number
n=int(input('Enter the number: '))
order= len(str(n))
temp=n
sum=0

while temp>0:
        digit=temp%10
        sum+= digit**order
        temp//=10

if n == sum:
    print(f"{n} Number is Amstrong")
else:
    print(f"{n} Number is not Amstrong")
