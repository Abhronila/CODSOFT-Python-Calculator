import math

def calculator():
    print("======SCIENTIFIC CALCULATOR======")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y )")
    print("7. Square Root (√x)")
    print("8. Factorial (x!)")
    print("9. Sine (sin x)")
    print("10. Logarithm base 10 (log10 x)")
    print("0. Exit")

    while True:
        choice = input("\nEnter operation number (0 to exit): ")

        if choice == '0':
            print("Exiting calculator..")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by 0!")
            elif choice == '5':
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif choice == '6':
                print(f"Result: {num1}^{num2} = {num1 ** num2}")
        
        #operations needing one input
        else:
            num = float(input("Enter nummber: "))

            if choice == '7':
                print(f"√{num} = {math.sqrt(num)}")
            elif choice == '8':
                print(f"{int(num)}! = {math.factorial(int(num))}")
            elif choice == '9':
                print(f"sin({num}) = {math.sin(math.radians(num))}")
            elif choice =='10':
                print(f"log10({num}) = {math.log10(num)}")
            else:
                print("❌Invalid choice!")

calculator()