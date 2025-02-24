

PI = 3.145
def Circle_area(radius):
    return (radius**2)*PI
r=int(input("Radius Value:"))
n=int(input("How many times to you want to call the Circle area function:"))
i=1
while i<n:
    Circle_area(r)
    n+=1
else:
    exit