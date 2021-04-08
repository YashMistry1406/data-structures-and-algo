class Solution:
    def solve(self, weights, values, capacity):

        def knap(cap,w,val,n):
            if cap==0 or n==0:
                return 0
            #checking if the value is previously calculated or not 
            if memo[n][cap]!=-1:
                return memo[n][cap]
            if w[n-1]>cap:
                memo[n][cap]=knap(cap,w,val,n-1)
                return memo[n][cap]
            else:
                memo[n][cap]=max(val[n-1]+knap(cap-w[n-1],w,val,n-1),knap(cap,w,val,n-1))
                return memo[n][cap]
        n=len(values)
        memo = [[-1 for i in range(capacity+ 1)] for j in range(n + 1)]
        return knap(capacity,weights,values,n)
