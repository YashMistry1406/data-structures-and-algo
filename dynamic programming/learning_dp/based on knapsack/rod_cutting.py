#the rod cutting problem is a variation of unbounded knapsack
#where we replace the following variable respectively,
#rod cutting --> unbounded knapsack
#n --> capacity
#prices --> values
#size --> capacity &weights
#if we look at the unbounded knapsack problem we can have the same item multiple times unlike 0-1 knapsack where there is now repetition
#Here in the rod cutting problem too we can have multiple rod of same length and thus we try and maximize among that.
#Implementation
#
#The implementation starts with initialising the size list that is the length at which cut can be made(in this problem it is not given that what length are allowed to be cut , so we take all the possibilities from 1 to n)
#eg:- sometimes it may be specified that the size should be [4,5,9] unlike in this problem where our size list is [1,2,3,4,5,6]
#
#Then comes the initialising of the 2d list, here i have used the tabulation or bottom up approach where there would be a list where all the values would be stored.
#dp=n X len(size) ,
#we would initialize the first row and column of the 2d list as zero as
#1 - it is not possible to create a list with zero element (for the row)
#2 - it is not possible to cut a rod with zero weight
#In the elif condition
#we are updating the 2d list where we are trying to maximize the cost
#
#if the current size is greater than the size of the rod we neglect it
#
#https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

class Solution:
    def solve(self, prices, n):
        size = [i for i in range(1, len(prices) + 1)]
        dp = [[0 for _ in range(n + 1)] for k in range(len(size) + 1)]

        for i in range(n + 1):
            for j in range(len(size) + 1):

                if i == 0 or j == 0:
                    dp[i][j] = 0

                elif size[i - 1] <= j:
                    dp[i][j] = max(prices[i - 1] + dp[i][j - size[i - 1]], dp[i - 1][j])

                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][len(size)]
