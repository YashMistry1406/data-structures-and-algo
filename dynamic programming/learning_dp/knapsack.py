#The following is the implentation of knapsack purely recursive without memoization an
#this will result to tle 
class Solution:
    def solve(self, weights, values, capacity):

        def knap(cap,w,val,n):
            #the base condition is that we have no capacity left or the weights array is over ie the lenght is 0
            if cap==0 or n==0:
                return 0
            #the choice logic is that when ever we have a weight that is greater than the capacity we will ignore that 
            if w[n-1]>cap:
                return knap(cap,w,val,n-1)# we return tothe recursive call and not updating the capacity
            else:
                #here we are choosing whether we will use the current weight that is less than the capacity
                #if we choose the weight it should be greater than the other choice which we iterate through
                return max(val[n-1]+knap(cap-w[n-1],w,val,n-1),knap(cap,w,val,n-1))
        n=len(values)
        return knap(capacity,weights,values,n)


