#https://www.hackerrank.com/challenges/sherlock-and-cost/problem
T = int(input())
for t in range(T):
    n = int(input())
    l = [int(x) for x in input().split()]
    lo = 0
    hi = 0
    for i in range(1,len(l)):
        lon = max(lo, hi + abs(1-l[i-1]))
        hin = max(lo + l[i]-1, hi + abs(l[i-1]-l[i]))
        lo, hi = lon, hin
        #print(lo, hi)
    print(max(lo, hi))