coin_set = [10,5,1]
# must be ordered from largest to smallest

def greedyCoinChange(amount, coins):
    coins_needed = {}
    coins.sort(reverse=True)

    for coin in coins:
        if coin <= amount:
            # if the coin value is less than or equal to the remaining required amount...

            neededAmt = amount // coin
            # ...get the maximum amount of that specific coin that can fit in the required amount...

            amount -= neededAmt * coin
            # ...and then subtract the value of those coins combined from the required amount.

            coins_needed[f"{str(coin)}¢ coin"] = neededAmt
            # then store in dict
    
    return coins_needed


inputAmt = int(input("How many cents? ¢: "))
print(greedyCoinChange(inputAmt, coin_set))