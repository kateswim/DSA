# In the first version we are not considering the budget

def max_profit(daily_prices):
    cash_not_owning_share = 0
    cash_owning_share = float('-inf')

    for price in daily_prices:

        strategy_buy = cash_not_owning_share - price
        strategy_sell = cash_owning_share + price

        strategy_hold = cash_owning_share
        strategy_avoid = cash_not_owning_share
    
        cash_owning_share = max(strategy_buy,strategy_hold)
        cash_not_owning_share = max(strategy_sell,strategy_avoid)

    
    return cash_not_owning_share

prices=[30,45,76,34,23,45,29,67,56,66,89]
print(max_profit(prices))

def max_profit(daily_prices, budget):
    cash_not_owning_share = budget
    cash_owning_share = float('-inf')

    for price in daily_prices:
        if cash_not_owning_share >= price:
            strategy_buy = cash_not_owning_share - price
        else:
            strategy_buy = float('-inf')

        strategy_sell = cash_owning_share + price

        strategy_hold = cash_owning_share
        strategy_avoid = cash_not_owning_share
    
        cash_owning_share = max(strategy_buy,strategy_hold)
        cash_not_owning_share = max(strategy_sell,strategy_avoid)

    final_cash = cash_not_owning_share
    profit = final_cash - budget

    return final_cash, profit

prices=[30,45,76,34,23,45,29,67,56,66,89]
print(max_profit(prices,29))