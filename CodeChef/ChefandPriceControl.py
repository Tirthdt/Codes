"""
Chef has N items in his shop (numbered 1 through N); for each valid i, the price of the i-th item is Pi. Since Chef has very loyal customers, all N items are guaranteed to be sold regardless of their price.

However, the government introduced a price ceiling K, which means that for each item i such that Pi>K, its price should be reduced from Pi to K.

Chef's revenue is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.


3 --> test cases
5 4 --> n, k
10 2 3 4 5
7 15
1 2 3 4 5 6 7
5 5
10 9 8 7 6

o/p:
7
0
15


"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    prices = [int(x) for x in input().split()]
    prices_after_ceiling = [x if x <= k else k for x in prices]
    print(sum(prices) - sum(prices_after_ceiling))
