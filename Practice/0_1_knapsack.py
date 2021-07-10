def testcase1():
    val = [50,100,150,200]
    wt = [8,16,32,40]
    W = 64
    return val,wt,W,len(wt)
def testcase2():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    return val,wt,W,len(wt)



def brute_force(val,wt,W,n):
    # base case is when the sack cannot carry weight or there is no items
    if n == 0 or W == 0 :
        return 0

    # case when the weight of the element is greater than the capacity
    elif wt[n-1]>W:
        return brute_force(val,wt,W,n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    # if item is taken, subtract that from recursive weight
    else:
        return(max(val[n - 1] + brute_force(val,wt,W-wt[n-1],n-1), brute_force(val,wt,W,n-1)))

if __name__ == '__main__':
    val, wt, W, n = testcase2()
    assert brute_force(val,wt,W,n) == 220, print(brute_force(val,wt,W,n))
