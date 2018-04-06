#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=49
#binary search
while True:
    try:
        n = int(input())
        p = int(input())
        lo = 0
        hi = 1123456789
        #
        while hi > lo:
            mid = (lo+hi)//2
            if pow(mid, n) == p:
                print(mid)
                break
            elif pow(mid, n) > p:
                hi = mid
            else:
                lo = mid+1
        
    except:
        break
