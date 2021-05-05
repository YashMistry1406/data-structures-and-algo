#the following code is just the variation in the subset()sum code 
#the only change we have made here is changing the true statements to 1 and False to 0 
#
def subset(stack,n,target):

    memo=[[0 for _ in range(target+1)] for z in range(n+1)]

    for i in range(n+1):
        memo[i][0]=1

    for j in range(1,target+1):
        memo[0][j]=0


    for i in range(1, n + 1):
        for j in range(1, target+ 1):
            if j<stack[i-1]:
                memo[i][j] = memo[i-1][j]
            if j>= stack[i-1]:
                memo[i][j] = (memo[i-1][j] + memo[i - 1][j-stack[i-1]])
               # in the above we have turned the or to + as we have the return type of int as compared to hte boolean in the subetsum code 

    return memo[n][target]

if __name__=='__main__':
    stack=[2,3,5,6,8,10]
    target=10
    n = len(stack)
    print(subset(stack,n,target))
