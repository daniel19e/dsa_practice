# given a target amount n and a list of distinct coin values, 
# whats the fewest coins needed to make the change amount
def coin_rec(target, coins):
    
    min_coins = target

    if target in coins:
        return 1
    
    else:
        # for every coin value that is <= my target value
        for i in coins:
            if i <= target:
                # add a coin count + recursive call
                num_coins = 1 + coin_rec(target-i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
            

    return min_coins
    

print(coin_rec(13,[1,5, 10])) #=> 1