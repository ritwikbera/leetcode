prices = [1,3,2,3]

def maxProfit(prices):
    profit = 0
    start = prices[0]
    for i in range(1, len(prices)+1):
        try:
            curr = prices[i]
        except IndexError:
            curr = -100
        prev = prices[i-1]
        if curr < prev:
            end = prev
            profit += end - start
            start = curr
        else:
            continue

    return profit 

print(maxProfit(prices))
