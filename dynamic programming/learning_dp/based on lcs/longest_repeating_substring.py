#the only change in this code with respect to that of lcs is in the first if of the loop where we add
#the condition ---> i!=j
# and other change in respect to lcs is that here we have to find the substring instead of subsequence 
#therefore in the else statement we reset the current space to 0 if the character doesnot match

class Solution:
    def solve(self, s):
        a,b=s,s
        m=len(s)
        n=len(s)
        dp=[[0 for _ in range(n+1)] for k in range(m+1)]
        result=0
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif a[i-1]==b[j-1] and i!=j:
                    dp[i][j]=dp[i-1][j-1]+1
                    result = max(result, dp[i][j])
                else:
                    dp[i][j]=0
        return result
