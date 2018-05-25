#Very interesting problem.  Never encountered this paradigm before.

maxq = 100002

small_thresh = 500

ys = [0]*maxq
#ys[y] gives you the number of lines that intersect y at an integer-x-coordinate. (for lines with large k)

    
from collections import defaultdict

small_ks = [defaultdict(int) for i in range(small_thresh+1)]
#small_ks[k][b] gives u the number of lines that match a line y=kx+b (for lines with small k)
#also note that b is modulo k.

n = int(input())
for i in range(n):
    inp = input().split()
    if inp[0] == '+':
        k, b = map(int, (inp[1], inp[2]))
        if k <= small_thresh:
            small_ks[k][b%k]+=1
        else:
            for j in range(b%k, maxq, k):
                ys[j]+=1
    elif inp[0] == '-':
        k, b = map(int, (inp[1], inp[2]))
        if k <= small_thresh:
            small_ks[k][b%k]-=1
        else:
            for j in range(b%k, maxq, k):
                ys[j]-=1
    else:
        q = int(inp[1])
        ans = 0
        for k in range(1,len(small_ks)):
            ans += small_ks[k][q%k]
        ans+=ys[q]
        print(ans)

