def stockmax(prices):
    n=len(prices)
    #finding greatest element towards right
    rle=[-1]*n
    rle[n-1]=prices[n-1]
    
    for i in range(n-2,-1,-1):
        if prices[i]<rle[i+1]:
            rle[i]=rle[i+1]
        else:
            rle[i]=prices[i]
    #calculating maximum profit
    max_profit=0
    for i in range(0,n):
        max_profit+=(rle[i]-prices[i])
    return max_profit