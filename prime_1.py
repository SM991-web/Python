def prime_not(num):
    if num<0 or num==0 or num==1:
        print(f"{num} is Not Prime")
    else:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                print(f"{num} is Not Prime")
            else:
                print(f"{num} is Prime")
if __name__=="__main__":    
    x=int(input())
    prime_not(x)