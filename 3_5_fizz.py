def fizz_3_5():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print("FizzBuzz",end=" , ")
        elif i%3==0:
            print("Fizz",end=" , ")
        elif i%5==0:
            print("Buzz",end=" , ")
        else:
            print(i,end=" , ")
if __name__=="__main__":    
    fizz_3_5()