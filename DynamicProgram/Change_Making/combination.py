from functools import lru_cache

def count_ways_to_pay(coins, amount):
    @lru_cache(maxsize=None)
    def count_ways_helper(index, amount):
        if amount == 0:
            return 1
        if amount < 0 or index == len(coins):
            return 0
        
        total_ways = 0
        coin = coins[index]
        for repeats in range(amount // coin + 1):
            payment = coin * repeats
            total_ways += count_ways_helper(index + 1, amount - payment)
            print(f"Using coin {coin}, repeats: {repeats}, remaining amount: {amount - payment}, total ways so far: {total_ways}")

        return total_ways
    return count_ways_helper(0, amount)

coins = [2, 5, 10]
amount = 17
print(count_ways_to_pay(coins, amount))  

        
        