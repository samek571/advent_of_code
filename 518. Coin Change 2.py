class Solution:
    def change(amount, coins) -> int:

        all = [0]* (amount+1)
        all[0] = 1

        for coin in coins:
            for atm in range(coin, amount+1):
                all[atm] += all[atm-coin]

        return all[amount]

    print(change(5, [1,2,3]))