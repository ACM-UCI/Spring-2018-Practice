# Enter your code here. Read input from STDIN. Print output to STDOUT
#PROBLEM STATEMENT IS WRONG.  the numbers are {1,2,5}, not {1,3,5} (at the time of this submission)

DP = [-1 for i in range(1001)]
DP[0] = 0
for i in range(1,len(DP)):
    cands = [DP[i-dx] for dx in [1,2,5] if (i-dx>=0 and DP[i-dx]>-1)]
    DP[i] = min(cands)+1
#print(DP[:100])

T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    true_ans = -1
    for edge_case, offset in [(0, 0), (1,1), (2,1)]:
        xsp = xs[:]
        argmin = xsp.index(min(xsp))
        xsp[argmin]-= edge_case
        
        s = min(xsp)
        xsp = [x-s for x in xsp]
        #xs.sort(reverse=True)
        ans = offset #quavo!
        for i in xsp:
            ans+= DP[i]
        if true_ans == -1:
            true_ans = ans
        else:
            true_ans = min(ans, true_ans)
    
    print(true_ans)