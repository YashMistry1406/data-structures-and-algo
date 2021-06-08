coins=list(map(int,input().split()))
amount=int(input())

def coinchange(coins,amt):
  dp=[[0 for _ in range(amt+1)] for k in range(len(coins)+1)]
  n=len(coins)
  for m in range(n):
    dp[m][0]=1
  for i in range(1,n+1):
    for j in range(1, amt+1):
      if coins[i-1]<=j:
        dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
      else:
        dp[i][j]=dp[i-1][j]
  return dp[n][amt]
print(coinchange(coins,amount))