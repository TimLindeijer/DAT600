from functools import cache

### Greedy coins
#Assumes coins array is sorted and positive integers
def GreedyCoins(coins, target):
    picked_coins = []
    while True:
        for i in range(len(coins)):
            if coins[i] > target:
                i -= 1
                break
            elif coins[i] == target:
                break
        best_coin = coins[i]
        if best_coin <= target:
            picked_coins.append(best_coin)
            target = target - best_coin
            print(f"Found coin: {best_coin}\nRemaining value: {target}")
        else:
            raise Exception("Failed to find suitable coin.")
        if target <= 0:
            break
    print(f"Best coins: {picked_coins}")

def DynamicCoins(coins, target):
    # Store the minimum number of coins needed to make each value
    @cache
    # Recursive function to find the minimum number of coins needed to make a value
    def MinCoins(target):
        if target <= 0:
            return None
        min_coins = None
        # Brute force, check all combinations for each coin
        for coin in coins:
            remainder = target - coin
            if remainder >= 0:
                remainder_result = MinCoins(remainder)
                if remainder_result is not None:
                    combination = remainder_result + [coin]
                    # Update min_coins if the combination is shorter
                    if min_coins is None or len(combination) < len(min_coins):
                        min_coins = combination
        # Print out the best combination
        print(f"Best coins: {min_coins}")
    return MinCoins(target)

if __name__ == "__main__":
    coinies = [1, 5, 11]
    targie = 15
    GreedyCoins(coinies, targie)
    DynamicCoins(coinies, targie)