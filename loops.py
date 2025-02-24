def prime(num):
    if num <= 1:
        print(num, "is not prime")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not prime")
            return
    print(num, "is prime")

x = int(input("Enter number to check prime:"))
prime(x)

# x  = ["apple","banana","Cherry","melon"]

# for i in x:
#     if i=="banana":
        
#         break
#     print(i)