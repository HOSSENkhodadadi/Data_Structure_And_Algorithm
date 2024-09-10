
# not efficient solution
def max_profit(Prices: list[int]) -> int:
    distances = []
    max_dist = 0
    max_i, max_j = 0, 0
    for i in range(len(prices)):
        # distances.append((i, prices[i], prices[i]))
        for j in range (i): 
            if prices[i]-prices[j]> max_dist: 
                max_dist = prices[i]-prices[j]
                max_i = prices[i]
                max_j = Prices[j] 
    return max_i, max_j, max_dist

# efficient solution
def max_profit_2 (prices: list[int])-> int:
    max_interest = 0
    min_price = prices[0]
    for i in range(1,len(prices)):
        if prices[i] < min_price:
            min = prices[i]
        elif prices[i] - min_price > max_interest :
            max_interest = prices[i] - min_price
    return max_interest




from random import randint
prices = []
for x in range (20):
    prices.append(randint(100, 200))

print(prices)
print(max_profit_2(prices))

