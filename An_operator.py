x = int(input())
y = int(input())
z = int(input())

if x>y and x>z:
    print(x,"is greater")
    if x==y or x==z:
        print("x is equal to y or z")
elif y>x and y>z:
    print(y,"is greater")
    if x==y or x==z:
        print("x is equal to y or z")
elif z>x and z>y:
    print(z,"is greater")
    if x==y or x==z:
        print("x is equal to y or z")
else:
    print("All are equal")