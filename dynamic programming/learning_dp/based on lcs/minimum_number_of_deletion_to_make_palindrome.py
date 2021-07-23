class Solution():
    def solve(self, a):
        m=len(a)
        b=a[::-1]
        n=len(b)


        dp=[[0 for _ in range(n+1)] for k in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                if a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return len(a)-dp[m][n]
