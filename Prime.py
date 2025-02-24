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