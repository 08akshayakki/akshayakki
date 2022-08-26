import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if n<0 or int(n)!=n:
        return "!not defined"
    if (n==0 or n==1):
        return n
    else:
        return n*factorial(n-1)
n=int(input("enter the number:"))
print("factorial of given number:", factorial(n))






