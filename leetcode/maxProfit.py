



def maxProfit(prices):
    if len(prices)<2:
        return 0

    best_gain = 0
    for i in range(0,len(prices)-1):
        if prices[i]>=prices[i+1]:
            continue

        cur_gain = max(prices[i+1:])-prices[i]
        if cur_gain<=0:
            continue

        best_gain = max(best_gain,cur_gain)

    return best_gain



best = maxProfit([7,1,5,3,6,4])
print(best)