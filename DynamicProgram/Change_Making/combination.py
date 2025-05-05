from functools import lru_cache

def count_ways_to_pay(coins, amount):
    @lru_cache(maxsize=None)
    def count_ways_helper(amount, index):
        if amount == 0:
            return 1
        if amount < 0 or index < 0:
            return 0
        
        
        