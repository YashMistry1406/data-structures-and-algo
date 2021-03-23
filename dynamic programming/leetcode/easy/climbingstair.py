#70. Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/solution/
class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        def solve(n,memo={}):
            if n==0:
                return 1 
            if n<0:
                return 0
            if n in memo:
                return memo[n]

            memo[n]=solve(n-1,memo)+solve(n-2,memo)

            return memo[n]
        return solve(n,memo={})

