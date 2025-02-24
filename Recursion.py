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
