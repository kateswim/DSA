# starts from last day and going down
def max_profit(daily_prices):
    def get_best_profit(day, have_stock):
        if day < 0:
            if not have_stock:
                return 0
            else:
                return -float('inf')
            
        price=daily_prices[day]
        if have_stock:
            strategy_buy=get_best_profit(day-1, False) - price
            strategy_hold=get_best_profit(day-1, True)
            return max(strategy_buy, strategy_hold)
        else:
            strategy_sell=get_best_profit(day-1, True) + price
            strategy_hold=get_best_profit(day-1, False)
            return max(strategy_sell, strategy_hold)

    return get_best_profit(len(daily_prices)-1, False)

prices=[30,45,76,34,23,45,29,67,56,66,89]
print(max_profit(prices))


