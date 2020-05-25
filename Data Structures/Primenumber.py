def isPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            return "Not prime"
    return "Prime"
test = int(input())
for _ in range(test):
    n = int(input())
    print(isPrime(n))