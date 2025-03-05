def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
def gen(n):
    for i in range(7):
        yield fibo(i)
if __name__=="__main__":
    x=int(input())
    fibo(x)

