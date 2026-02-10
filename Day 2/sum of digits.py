def sumOfDigits(n,s):
    if n==0:
        return 0
    else:
        return (s+(n%10))+sumOfDigits(n//10,s)
n=int(input())
s=0
print(sumOfDigits(n,s))