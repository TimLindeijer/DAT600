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

if __name__ == "__main__":
    coinies = [1, 5, 11]
    targie = 15
    GreedyCoins(coinies, targie)