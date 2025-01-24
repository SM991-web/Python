def calculator(num1,num2):
    num1 = int(input())
    num2 = int(input())

    print("Choose The Operation for the numbers",num1,"and",num2,"\n")

    print("\tChoose :\t\n")
    print("\tAddition '+'")
    print("\tSubtraction '-'")
    print("\tDivision '/'")
    print("\tMultiplication 'x'")

    Choose = input("\t\t\tEnter choice:\t\t\t")

    if Choose == "+":
        print(num1,'+',num2,'=',num1+num2)
    elif Choose == "-":
        if num1>num2:
            print(num1,'-',num2,'=',num1-num2)
        elif num2>num1:
            print(num2,'-',num1,'=',num2-num1)
    elif Choose.lower() == "x":
        print(num1,'x',num2,'=',num1*num2)
    elif Choose == "/":
        if num2 == 0:
            print("Not divisible")
        else:
            print(num1,'/',num2,'=',num1/num2)


