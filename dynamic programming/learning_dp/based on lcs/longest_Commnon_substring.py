class Solution:
    def solve(self, s0, s1):
        a,b=s0,s1
        m=len(a)
        n=len(b)

        dp=[[0 for _ in range(n+1)] for k in range(m+1)]
        result=0
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif a[i-1]==b[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    result = max(result, dp[i][j])
                #if character is not same of the both the strings we neglect the postion and 
                #fill it with 0
                else:
                    dp[i][j]=0
        return result

