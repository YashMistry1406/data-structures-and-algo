values=list(map(int,input().split()))
weights=list(map(int,input().split()))
capacity=int(int(input()))
n=len(values)
memo=[[0 for _ in range(capacity+1)] for k in range(n+1)]

for i in range(n+1):
    for j in range(capacity+1):
        if i==0 and j==0:
            memo[i][j]=0
        elif weights[n-1]<=j:
            memo[i][j]=max(values[n-1]+ memo[n-1][j-weights[i-1]],memo[i-1][j])
        else:
            memo[i][j]=memo[i-1][j]

print(memo[n][capacity])


'''
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]
'''
