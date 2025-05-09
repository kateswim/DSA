from functools import lru_cache

def count_ways_to_pay(coins, amount):
    @lru_cache(maxsize=None)
    def count_ways_helper(amount):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        
        total_ways = 0
        for coin in coins:
            total_ways += count_ways_helper(amount - coin)
            print(f"Using coin {coin}, remaining amount: {amount - coin}, total ways so far: {total_ways}")
        
        return total_ways
    return count_ways_helper(amount)

coins = [2, 5, 10]
amount = 12
print(count_ways_to_pay(coins, amount))