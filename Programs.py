# ASSIGNMENT - 01 SUBJECT - CODING SKILL  SUBMITTED BY - SNEHANSHU MUKHOPADHYAY  ROLL - 24CS003230    BRANCH - CSE AI and ML  SEMESTER - 2ND  DATE - 15/02/2025

# SUBMITTED TO - DIPESH VAYA SIR 

# Simple Calculator Program using if-else and function concept

def CP():
    print("Welcome to the Calculator Program")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose The Operation for the numbers", num1, "and", num2, "\n")

    print("\tChoose :\t\n")
    print("\tAddition '+'")
    print("\tSubtraction '-'")
    print("\tDivision '/'")
    print("\tMultiplication 'x'")

    Choose = input("\t\tEnter choice: ")

    if Choose == "+":
        print(num1, '+', num2, '=', num1 + num2)
    elif Choose == "-":
        print(num1, '-', num2, '=', num1 - num2)
    elif Choose.lower() == "x":
        print(num1, 'x', num2, '=', num1 * num2)
    elif Choose == "/":
        if num2 == 0:
            print("Not divisible")
        else:
            print(num1, '/', num2, '=', num1 / num2)
    else:
        print("Invalid Input")

if __name__ == "__main__":
    CP()
    Choice = input("Do you want to use again the calculator program? (Y/N) ")
    while Choice.lower() == "y" or Choice.lower() == "yes":
        CP()
        Choice = input("Do you want to use again the calculator program? (Y/N) ")
    else:
        print("Thank you for using the program")
        print("Exit")

"""


Output:

Welcome to the Calculator Program
Enter the first number: 3
Enter the second number: 5
Choose The Operation for the numbers 3.0 and 5.0 

        Choose :

        Addition '+'
        Subtraction '-'
        Division '/'
        Multiplication 'x'
                Enter choice: +
3.0 + 5.0 = 8.0

Do you want to use again the calculator program? (Y/N) y
Welcome to the Calculator Program
Enter the first number: 5
Enter the second number: 6
Choose The Operation for the numbers 5.0 and 6.0 

        Choose :

        Addition '+'
        Subtraction '-'
        Division '/'
        Multiplication 'x'
                Enter choice: -
5.0 - 6.0 = -1.0

Do you want to use again the calculator program? (Y/N) n
Thank you for using the program
Exit


"""


# Factorial Program System


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":    
    print(f"Welcome to Factorial Program")
    
    while True:
        number = int(input("Enter Number: "))
        print(f"Factorial of {number}:", factorial(number))
        
        ch = input("Do you want to find the factorial of another number? (y/n): ")
        if ch.lower() != "y":
            print("Thank you for using the program")
            exit()




"""


Output:

Welcome to Factorial Program
Enter Number: 3
Factorial of 3: 6

Do you want to find the factorial of another number? (y/n): y
Enter Number: 6
Factorial of 6: 720

Do you want to find the factorial of another number? (y/n): y
Enter Number: 5
Factorial of 5: 120

Do you want to find the factorial of another number? (y/n): n
Thank you for using the program


"""



# Fibonacci Program System

def fibonacci(n):
    if n <= 0:
        return "Invalid input, please enter a positive number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":    
    print(f"Welcome to Fibonacci Program")
    
    while True:
        number = int(input("Enter the position (n) for Fibonacci sequence: "))
        print(f"Fibonacci number at position {number}:", fibonacci(number))
        
        ch = input("Do you want to find another Fibonacci number? (y/n): ")
        if ch.lower() != "y":
            print("Thank you for using the program")
            exit()



"""


Output:

Welcome to Fibonacci Program
Enter the position (n) for Fibonacci sequence: 3
Fibonacci number at position 3: 1

Do you want to find another Fibonacci number? (y/n): n
Thank you for using the program


"""



# Prime numberb Program System

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return "Not Prime"
        else:
            return "Prime"
    else:
        return "Not Prime"
if __name__=="__main__":
    print("Welcome to the Prime Number Program")
    while True:
        number = int(input("Enter Number: "))
        print(f"{number} is {prime(number)}")
        ch = input("Do you want to check another number? (y/n): ")
        if ch.lower() != "y":
            print("Thank you for using the program")
            exit()


"""


Output:

Welcome to the Prime Number Program
Enter Number: 3
3 is Prime

Do you want to check another number? (y/n): y
Enter Number: 2
2 is Prime

Do you want to check another number? (y/n): y
Enter Number: 6
6 is Not Prime

Do you want to check another number? (y/n): n
Thank you for using the program


"""