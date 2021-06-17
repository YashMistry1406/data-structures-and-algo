class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a,b=word1,word2
        m=len(a)
        n=len(b)

        dp=[[0 for _ in range(n+1)] for k in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        temp=dp[m][n]
        ans=abs((m-temp)+(n-temp))
        return ans
#583. Delete Operation for Two Strings
#Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
#
#In one step, you can delete exactly one character in either string.
#
# 
#
#Example 1:
#
#Input: word1 = "sea", word2 = "eat"
#Output: 2
#Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#Example 2:
#
#Input: word1 = "leetcode", word2 = "etco"
#Output: 4
# 
#
#Constraints:
#
#1 <= word1.length, word2.length <= 500
#word1 and word2 consist of only lowercase English letters.
