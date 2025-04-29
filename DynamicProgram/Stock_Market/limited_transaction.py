def max_profit(daily_price, tx_limit):
    cash_not_owning_share = [-float('inf')] * (tx_limit + 1)
    cash_not_owning_share[0] = 0

    cash_owning_share = [-float('inf')] * (tx_limit + 1)
    print(cash_not_owning_share)
    print(cash_owning_share)

    for price in daily_price:
        cash_not_owning_share_next = [-float('inf')] * (tx_limit + 1)
        cash_owning_share_next = [-float('inf')] * (tx_limit + 1)
        
        for prev_tx_count in range(tx_limit):
            
            strategy_buy = cash_not_owning_share[prev_tx_count] - price
            strategy_sell = cash_owning_share[prev_tx_count] + price

            strategy_hold = cash_owning_share[prev_tx_count]
            strategy_avoid = cash_not_owning_share[prev_tx_count]

            if prev_tx_count < tx_limit:
                cash_not_owning_share_next[prev_tx_count + 1] = max(cash_not_owning_share_next[prev_tx_count + 1], strategy_sell)
            
            cash_not_owning_share_next[prev_tx_count] = max(cash_not_owning_share_next[prev_tx_count], strategy_avoid)
            cash_owning_share_next[prev_tx_count] = max(cash_owning_share_next[prev_tx_count], strategy_buy, strategy_hold)  

            print(cash_not_owning_share_next)
            print(cash_owning_share_next)
            
            cash_not_owning_share = cash_not_owning_share_next
            cash_owning_share = cash_owning_share_next

    return max(cash_not_owning_share)

prices=[30,45,76,34,23,45,29,67,56,66,89]
print(max_profit(prices,4))