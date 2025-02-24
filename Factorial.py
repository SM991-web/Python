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

