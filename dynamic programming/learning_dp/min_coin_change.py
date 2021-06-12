def min_coin_change(coins,amt):
    dp=[[0 for _ in range(amt+1)] for m in range(coins+1)]
    n=len(coins)
    for m in range(1,n+1):
        dp[m][0]=0
    for l in range(0,amt):
        dp[0][l]=float('inf')
    for i in range(1,n+1):
        for j in range(1,amt+1):
            if coins[i-1]<=j:
                dp[i][j]=min(dp[i][coins[i-1]]+1,dp[i-1][j])
            else:
                  return dp[i-1][j]
    return dp[n][amt]


