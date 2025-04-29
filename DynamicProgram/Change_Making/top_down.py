def make_change(coins, amount):
    if not amount:
        return []
    if amount < 0: 
        return None
    optimal_result = None

    for coin in coins:
        result= make_change(coins, amount - coin)
        if result is not None: # if amount < 0
            result = result + [coin]

            if optimal_result is None or len(result) < len(optimal_result):
                optimal_result = result
                print(f"Optimal result is: {optimal_result}")

    return optimal_result


coins = [2, 5, 10] 
amount = 15
print(make_change(coins, amount))


from functools import lru_cache

def make_change(coins, amount):

    @lru_cache(maxsize=None)
    def helper(amount):
        if not amount:
            return []      
        if amount < 0:
            return None
        
        optimal_result = None
        for coin in coins:
            result=helper(amount - coin)
            if result is not None:
                result = result + [coin]

                if optimal_result is None or len(result) < len(optimal_result):
                    optimal_result = result
                    print(f"Optimal result is: {optimal_result}")

        return optimal_result
    
    return helper(amount)

coins = [2, 5, 10] 
amount = 15
print(make_change(coins, amount))
