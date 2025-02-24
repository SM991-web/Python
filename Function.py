def function(a=None):
    if a is None:
        a=int(input())
    for i in range(1,11):
        print(a,"x",i,"=",a*i)
    y = lambda num: num + num
    print("Lambda function result:", y(4))
function(9)

print("Return value of function(7):", function(7))
# def func():
#     print("hr")
#     return  10
# func()
