while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break
    import math
    prime = True
    for i in range(2,int(math.sqrt(p))+1):
        if p%i == 0:
            prime = False
    print("yes" if pow(a, p, p) == a%p and not prime else "no")

