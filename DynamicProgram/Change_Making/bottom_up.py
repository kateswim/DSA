def make_change(coins, amount):
    solutions = [None] * (amount + 1)
    solutions[0] = []

    paid = 0

    while paid < amount:
        if solutions[paid] is not None:
            for coin in coins:
                next_paid = paid + coin

                if next_paid > amount:
                    continue

                if solutions[next_paid] is None or len(solutions[next_paid]) > len(solutions[paid]) + 1:
                    solutions[next_paid] = solutions[paid] + [coin]
                    print(f"Paid: {paid}, Coin: {coin}, Next Paid: {next_paid}, Solutions: {solutions[next_paid]}")

        paid += 1
    return solutions[amount]         

coins = [2, 5, 10] 
amount = 15
print(make_change(coins, amount))


from collections import deque

def simplest_change(coins, amount):
    solutions = {0: []}
    amounts_to_be_handled = deque([0])

    while amounts_to_be_handled:
        paid = amounts_to_be_handled.popleft()
        solution = solutions[paid]
        if paid == amount:
            return solution
        
        for coin in coins:
            next_paid = paid + coin
            if next_paid > amount:
                continue

            if next_paid not in solutions:
                solutions[next_paid] = solution + [coin]
                amounts_to_be_handled.append(next_paid)

    return None

coins = [2, 5, 10] 
amount = 15
print(simplest_change(coins, amount))
