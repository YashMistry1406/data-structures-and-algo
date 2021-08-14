class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        m=len(a)
        n=len(b)
        if m==0:
            return True
        if n==0:
            return False

        dp=[[0 for _ in range(n+1)] for k in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                if a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n] == min(m,n)

