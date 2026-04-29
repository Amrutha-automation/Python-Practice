# Menu-driven program combining all features

from basics.even_odd import check_even_odd
from basics.prime_number import is_prime
from basics.fibonacci import fibonacci
from basics.factorial import factorial


def menu():
    print("\n--- Python Practice Menu ---")
    print("1. Even/Odd Check")
    print("2. Prime Check")
    print("3. Fibonacci Series")
    print("4. Factorial")
    print("5. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter number: "))
        print(check_even_odd(n))

    elif choice == "2":
        n = int(input("Enter number: "))
        print("Prime" if is_prime(n) else "Not Prime")

    elif choice == "3":
        n = int(input("Enter number of terms: "))
        print(fibonacci(n))

    elif choice == "4":
        n = int(input("Enter number: "))
        print(factorial(n))

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
